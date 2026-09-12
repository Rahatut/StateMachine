# DWS-Bench

DWS-Bench is a deterministic benchmark for dynamic world-state reasoning in
small language models. It generates symbolic state-transition trajectories,
validates them against explicit structural contracts, renders them as natural
language, and evaluates model answers against simulator-derived ground truth.

The simulator is the source of truth: the renderer never defines or changes an
instance's gold answer.

## Project Structure

| Path | Purpose |
|---|---|
| `world/` | World state, operations, and replay logic |
| `generator/` | Query specifications, trajectory generation, sampling, and validation |
| `render/` | Natural-language rendering and templates |
| `eval/` | Model configurations, inference engines, and evaluation harness |
| `analysis/` | Accuracy analysis, failure onset, and error classification |
| `experiments/` | RQ1-RQ5 dataset-generation scripts |
| `data/` | Generated JSONL benchmark datasets |
| `results/` | Evaluation predictions, metrics, and reports |
| `diagrams/` | Conceptual thesis-diagram source files |
| `report/` | LaTeX thesis source and figure assets |
| `test/` | Smoke, invariant, factor, analysis, and pipeline tests |

## Requirements

Python 3.10 or newer is recommended. Install the declared dependencies from the
repository root:

```bash
python3 -m pip install -r requirements.txt
```

The optional model backends in `requirements.txt` are only needed for real
inference. Mock evaluation and the generation tests do not require a GPU.

## Benchmark Design

Each accepted instance records the realized factors:

- `E`: entity load
- `T`: target-relevant update depth
- `D`: state-changing distractor updates
- `N`: text-only narrative distractors
- `V`: revision complexity
- `U`: total canonical updates
- `L`: rendered word-count proxy

The benchmark supports eight operations: `PUT`, `MOVE`, `REMOVE`, `UNDO`,
`REDO`, `SPLIT`, `MERGE`, and `SWAP`.

### Research Sweeps

| Sweep | Conditions | Default records |
|---|---|---:|
| RQ1: temporal depth | `T` in `{2, 4, 6, 8, 12, 16}` | 300 |
| RQ2: revision | `T` in `{4, 8, 12, 16}` with revision | 200 |
| RQ3: distractor interference | `D` in `{4, 8, 16}` plus matched narrative distractors | 200 |
| RQ4: entity load | `E` in `{2, 3, 4, 5}`, with `T=8`, `D=4` | 200 |
| RQ5: structural pilot | split, merge, swap, undo, and undo-redo families | 250 |
| **Full benchmark** | All generated sweeps | **1,150** |

RQ5 requests `T=8`, but the frozen records do not realize identical depth for
every family: `split_chain` records have `T_actual=7` and `D_actual=1`, while
the other four pilot families have `T_actual=8`.

## Generate Data

Run reachability probes without writing the benchmark:

```bash
python3 generate_all.py --dry-run
```

Generate the complete default suite and aggregate it into
`data/full_benchmark.jsonl`:

```bash
python3 generate_all.py
```

The generated files are:

```text
data/rq1_depth/rq1_depth.jsonl             300 records
data/rq2_revision/rq2_revision.jsonl       200 records
data/rq3_distractor/rq3_distractor.jsonl   200 records
data/rq4_entity_load/rq4_entity_load.jsonl 200 records
data/rq5_pilot/rq5_pilot.jsonl             250 records
data/full_benchmark.jsonl                1,150 records
```

## Run Evaluation

The evaluation CLI supports these registered model keys:

```text
qwen2.5-0.5b
qwen2.5-3b
qwen2.5-7b
llama-3.2-3b (not evaluated)
olmo-2-1b (not evaluated)
```

The default generation configuration uses deterministic decoding and
`max_new_tokens=256`. Run a dependency-free mock evaluation with:

```bash
python3 run_eval.py --model qwen2.5-0.5b --dataset full --mock
```

Run real inference on a supported device with:

```bash
python3 run_eval.py \
  --model qwen2.5-3b \
  --dataset full \
  --device cuda \
  --precision bfloat16
```

Dataset shortcuts currently include `full`, `rq1`, `rq2`, `rq3`, and `rq5`.
RQ4 has no shortcut, so pass its JSONL path explicitly:

```bash
python3 run_eval.py \
  --model qwen2.5-0.5b \
  --dataset data/rq4_entity_load/rq4_entity_load.jsonl \
  --mock
```

Use `--cot` to enable the structured chain-of-thought prompt. Evaluation output
is written under `results/<model_name>/` and includes predictions JSONL, metrics
JSON, a Markdown report, and an audit CSV.

## Current Evaluation Status

The repository contains registered configurations for five model families, but
the stored thesis results currently cover the three Qwen2.5 variants under
zero-shot and CoT prompting. The report presents evaluated results for RQ1-RQ3
and the RQ5 structural pilot. RQ4 data generation is complete, but corresponding
model-output summaries are still pending.

The naturalistic reference work is treated as a pilot/descriptive analysis;
there are no model-level ProPara results in the current evaluation artifacts.

## Tests

Run the master test and smoke-test collection:

```bash
python3 test/run_all.py
```

The master runner covers the smoke, trajectory, invariant, measured-factor,
analysis, and evaluation-pipeline tests. The evaluator-v2 test is run separately
with `pytest`:

```bash
python3 -m pytest test/test_evaluator_v2.py
```

## Thesis Figures and Report

The six conceptual diagrams in `diagrams/` use the local renderer in
`diagrams/helpers.py`. Generate them from the repository root:

```bash
for script in diagrams/fig*.py; do
  python3 "$script" || exit 1
done
```

The scripts write PNG and PDF files to `report/images/thesis_figures/`. The
analysis plots already stored in that directory are separate from these six
conceptual diagrams.

Build the thesis from the `report/` directory:

```bash
cd report
pdflatex -interaction=nonstopmode -halt-on-error main.tex
biber main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Reproducibility Notes

Generation records requested and realized factors, random seeds where applicable,
and validation outcomes. Evaluation records model configuration, prompt mode,
decoding settings, extracted answers, final correctness, and step-wise results.
Keep generated data and result directories versioned or archived with the code
revision used to produce them when reporting new experiments.
