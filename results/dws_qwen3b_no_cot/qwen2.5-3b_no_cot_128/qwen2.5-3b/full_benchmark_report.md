# Evaluation Report: `qwen2.5-3b` on `full_benchmark`

- **Model ID**: `Qwen/Qwen2.5-3B-Instruct` (3.0B params)
- **Total Instances**: 1150
- **Overall Accuracy (A_final)**: **25.65%**
- **Runtime**: 1609.49s

## Trajectory Family Accuracies

| Trajectory Family | Instances | Correct | Accuracy |
|---|---|---|---|
| `basic_chain` | 300 | 129 | **43.0%** |
| `revision` | 200 | 74 | **37.0%** |
| `interleaved_chain` | 400 | 0 | **0.0%** |
| `split_chain` | 50 | 4 | **8.0%** |
| `merge_chain` | 50 | 9 | **18.0%** |
| `swap_chain` | 50 | 10 | **20.0%** |
| `undo_chain` | 50 | 29 | **58.0%** |
| `undo_redo_chain` | 50 | 40 | **80.0%** |

## RQ1 Temporal Depth Degradation Curve
**Failure Onset (L_T @ τ=0.70)**: `2`

| Depth (T) | Accuracy |
|---|---|
| T = 2 | 2.0% |
| T = 4 | 16.0% |
| T = 6 | 44.0% |
| T = 8 | 72.0% |
| T = 12 | 92.0% |
| T = 16 | 32.0% |

## RQ2 Revision Complexity Curve

| Depth (T) | Accuracy (V ≥ 2) |
|---|---|
| T = 4 | 24.0% |
| T = 8 | 36.0% |
| T = 12 | 82.0% |
| T = 16 | 6.0% |

## RQ3 Distractor Interference Curve
**Failure Onset (L_D @ τ=0.70)**: `4`

| Distractors (D) | Accuracy |
|---|---|
| D = 4 | 0.0% |
| D = 8 | 0.0% |
| D = 16 | 0.0% |
