# Evaluation Report: `qwen2.5-0.5b` on `full_benchmark`

- **Model ID**: `Qwen/Qwen2.5-0.5B-Instruct` (0.5B params)
- **Total Instances**: 1150
- **Overall Accuracy (A_final)**: **40.78%**
- **Runtime**: 2305.12s

## Trajectory Family Accuracies

| Trajectory Family | Instances | Correct | Accuracy |
|---|---|---|---|
| `basic_chain` | 300 | 147 | **49.0%** |
| `revision` | 200 | 79 | **39.5%** |
| `interleaved_chain` | 400 | 111 | **27.8%** |
| `split_chain` | 50 | 6 | **12.0%** |
| `merge_chain` | 50 | 34 | **68.0%** |
| `swap_chain` | 50 | 28 | **56.0%** |
| `undo_chain` | 50 | 30 | **60.0%** |
| `undo_redo_chain` | 50 | 34 | **68.0%** |

## RQ1 Temporal Depth Degradation Curve
**Failure Onset (L_T @ τ=0.70)**: `4`

| Depth (T) | Accuracy |
|---|---|
| T = 2 | 100.0% |
| T = 4 | 66.0% |
| T = 6 | 24.0% |
| T = 8 | 22.0% |
| T = 12 | 46.0% |
| T = 16 | 36.0% |

## RQ2 Revision Complexity Curve

| Depth (T) | Accuracy (V ≥ 2) |
|---|---|
| T = 4 | 48.0% |
| T = 8 | 40.0% |
| T = 12 | 40.0% |
| T = 16 | 30.0% |

## RQ3 Distractor Interference Curve
**Failure Onset (L_D @ τ=0.70)**: `4`

| Distractors (D) | Accuracy |
|---|---|
| D = 4 | 29.0% |
| D = 8 | 38.0% |
| D = 16 | 10.0% |
