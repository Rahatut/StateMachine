# Evaluation Report: `qwen2.5-0.5b` on `full_benchmark`

- **Model ID**: `Qwen/Qwen2.5-0.5B-Instruct` (0.5B params)
- **Total Instances**: 1150
- **Overall Accuracy (A_final)**: **0.17%**
- **Runtime**: 778.42s

## Trajectory Family Accuracies

| Trajectory Family | Instances | Correct | Accuracy |
|---|---|---|---|
| `basic_chain` | 300 | 0 | **0.0%** |
| `revision` | 200 | 2 | **1.0%** |
| `interleaved_chain` | 400 | 0 | **0.0%** |
| `split_chain` | 50 | 0 | **0.0%** |
| `merge_chain` | 50 | 0 | **0.0%** |
| `swap_chain` | 50 | 0 | **0.0%** |
| `undo_chain` | 50 | 0 | **0.0%** |
| `undo_redo_chain` | 50 | 0 | **0.0%** |

## RQ1 Temporal Depth Degradation Curve
**Failure Onset (L_T @ τ=0.70)**: `2`

| Depth (T) | Accuracy |
|---|---|
| T = 2 | 0.0% |
| T = 4 | 0.0% |
| T = 6 | 0.0% |
| T = 8 | 0.0% |
| T = 12 | 0.0% |
| T = 16 | 0.0% |

## RQ2 Revision Complexity Curve

| Depth (T) | Accuracy (V ≥ 2) |
|---|---|
| T = 4 | 2.0% |
| T = 8 | 0.0% |
| T = 12 | 2.0% |
| T = 16 | 0.0% |

## RQ3 Distractor Interference Curve
**Failure Onset (L_D @ τ=0.70)**: `4`

| Distractors (D) | Accuracy |
|---|---|
| D = 4 | 0.0% |
| D = 8 | 0.0% |
| D = 16 | 0.0% |
