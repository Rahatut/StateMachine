# Evaluation Report: `qwen2.5-7b` on `full_benchmark`

- **Model ID**: `Qwen/Qwen2.5-7B-Instruct` (7.0B params)
- **Total Instances**: 1150
- **Overall Accuracy (A_final)**: **11.39%**
- **Runtime**: 1395.46s

## Trajectory Family Accuracies

| Trajectory Family | Instances | Correct | Accuracy |
|---|---|---|---|
| `basic_chain` | 300 | 24 | **8.0%** |
| `revision` | 200 | 25 | **12.5%** |
| `interleaved_chain` | 400 | 78 | **19.5%** |
| `split_chain` | 50 | 0 | **0.0%** |
| `merge_chain` | 50 | 0 | **0.0%** |
| `swap_chain` | 50 | 4 | **8.0%** |
| `undo_chain` | 50 | 0 | **0.0%** |
| `undo_redo_chain` | 50 | 0 | **0.0%** |

## RQ1 Temporal Depth Degradation Curve
**Failure Onset (L_T @ τ=0.70)**: `2`

| Depth (T) | Accuracy |
|---|---|
| T = 2 | 0.0% |
| T = 4 | 30.0% |
| T = 6 | 8.0% |
| T = 8 | 4.0% |
| T = 12 | 6.0% |
| T = 16 | 0.0% |

## RQ2 Revision Complexity Curve

| Depth (T) | Accuracy (V ≥ 2) |
|---|---|
| T = 4 | 40.0% |
| T = 8 | 0.0% |
| T = 12 | 10.0% |
| T = 16 | 0.0% |

## RQ3 Distractor Interference Curve
**Failure Onset (L_D @ τ=0.70)**: `4`

| Distractors (D) | Accuracy |
|---|---|
| D = 4 | 22.3% |
| D = 8 | 22.0% |
| D = 16 | 0.0% |
