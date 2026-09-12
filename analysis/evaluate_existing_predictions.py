"""Re-score saved DWS-Bench generations with the instance-aware Evaluator v2."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, Iterable, List

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from eval.evaluator_v2 import extract_instance_answer, normalize_text


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def load_instances(path: Path) -> Dict[str, Dict[str, Any]]:
    return {row["instance_id"]: row for row in load_jsonl(path)}


def infer_condition(prediction_path: Path) -> Dict[str, Any]:
    condition = prediction_path.parent.parent.name
    match = re.match(r"(?P<model>.+?)_(?P<cot>no_cot|cot)_(?P<tokens>\d+)$", condition)
    if not match:
        raise ValueError(f"Cannot infer model condition from {prediction_path}")
    return {
        "model": match.group("model"),
        "cot": match.group("cot") == "cot",
        "max_new_tokens": int(match.group("tokens")),
        "condition": condition,
    }


def candidate_answers(instance: Dict[str, Any]) -> List[str]:
    values = list(instance.get("step_wise_gold_answers", []))
    values.append(instance.get("gold_answer", ""))
    unique: Dict[str, str] = {}
    for value in values:
        normalized = normalize_text(value)
        if normalized:
            unique[normalized] = str(value)
    return list(unique.values())


def score_prediction(
    prediction: Dict[str, Any],
    instance: Dict[str, Any],
    chain_of_thought: bool,
) -> Dict[str, Any]:
    extraction = extract_instance_answer(
        prediction.get("raw_prediction", ""),
        candidate_answers(instance),
        chain_of_thought=chain_of_thought,
    )
    gold = normalize_text(instance.get("gold_answer", ""))
    semantic_correct = normalize_text(extraction.answer) == gold
    strict_correct = semantic_correct and extraction.protocol_compliant
    result = dict(prediction)
    result.update({
        "model": prediction.get("model") or instance.get("model"),
        "semantic_correct": semantic_correct,
        "strict_correct": strict_correct,
        "protocol_compliant": extraction.protocol_compliant,
        "answer_extracted": extraction.answer,
        "extraction_method": extraction.method,
        "has_final_answer": extraction.has_final_answer,
        "gold_answer": instance.get("gold_answer", ""),
        "family": instance.get("family", prediction.get("family", "")),
        "depth": instance.get("measured_factors", {}).get(
            "T_actual", instance.get("requested_factors", {}).get("T")
        ),
    })
    return result


def aggregate(rows: Iterable[Dict[str, Any]], keys: List[str]) -> List[Dict[str, Any]]:
    buckets: Dict[tuple, List[Dict[str, Any]]] = {}
    for row in rows:
        buckets.setdefault(tuple(row.get(key) for key in keys), []).append(row)
    output = []
    for values, bucket in sorted(buckets.items(), key=lambda item: str(item[0])):
        token_values = [row.get("generated_tokens") for row in bucket if row.get("generated_tokens") is not None]
        output.append({
            **dict(zip(keys, values)),
            "instances": len(bucket),
            "semantic_accuracy": mean(bool(row["semantic_correct"]) for row in bucket),
            "strict_accuracy": mean(bool(row["strict_correct"]) for row in bucket),
            "protocol_compliance": mean(bool(row["protocol_compliant"]) for row in bucket),
            "correct_given_protocol": (
                sum(bool(row["strict_correct"]) for row in bucket)
                / sum(bool(row["protocol_compliant"]) for row in bucket)
                if any(row["protocol_compliant"] for row in bucket) else None
            ),
            "invalid_rate": mean(not bool(row["protocol_compliant"]) for row in bucket),
            "truncation_rate": mean(row.get("finish_reason") == "length" for row in bucket),
            "mean_generated_tokens": mean(token_values) if token_values else None,
            "median_generated_tokens": median(token_values) if token_values else None,
        })
    return output


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    if not rows:
        return
    fields = sorted({key for row in rows for key in row})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=Path, default=Path("data/full_benchmark.jsonl"))
    parser.add_argument("--predictions-root", type=Path, default=Path("."))
    parser.add_argument("--output-dir", type=Path, default=Path("evaluator_v2_results"))
    args = parser.parse_args()

    instances = load_instances(args.dataset)
    prediction_files = sorted(args.predictions_root.glob("**/*_predictions.jsonl"))
    if not prediction_files:
        raise FileNotFoundError("No saved prediction JSONL files found.")

    all_rows: List[Dict[str, Any]] = []
    for prediction_path in prediction_files:
        condition = infer_condition(prediction_path)
        for prediction in load_jsonl(prediction_path):
            instance = instances[prediction["instance_id"]]
            row = score_prediction(prediction, instance, condition["cot"])
            row.update(condition)
            all_rows.append(row)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "evaluator_v2_predictions.csv", all_rows)
    write_csv(args.output_dir / "evaluator_v2_summary.csv", aggregate(all_rows, ["model", "cot", "max_new_tokens", "condition"]))
    write_csv(args.output_dir / "evaluator_v2_family.csv", aggregate(all_rows, ["model", "cot", "max_new_tokens", "family"]))
    write_csv(args.output_dir / "evaluator_v2_depth.csv", aggregate(all_rows, ["model", "cot", "max_new_tokens", "depth"]))
    print(f"Scored {len(all_rows)} predictions across {len(prediction_files)} conditions.")
    print(f"Saved Evaluator v2 outputs to {args.output_dir}")


if __name__ == "__main__":
    main()
