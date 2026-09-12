# Evaluation Report: `qwen2.5-7b` on `full_benchmark`

- **Model ID**: `Qwen/Qwen2.5-7B-Instruct` (7.0B params)
- **Total Instances**: 1150
- **Overall Accuracy (A_final)**: **9.74%**
- **Runtime**: 4514.62s

## Trajectory Family Accuracies

| Trajectory Family | Instances | Correct | Accuracy |
|---|---|---|---|
| `basic_chain` | 300 | 28 | **9.3%** |
| `revision` | 200 | 8 | **4.0%** |
| `interleaved_chain` | 400 | 65 | **16.2%** |
| `split_chain` | 50 | 4 | **8.0%** |
| `merge_chain` | 50 | 3 | **6.0%** |
| `swap_chain` | 50 | 3 | **6.0%** |
| `undo_chain` | 50 | 0 | **0.0%** |
| `undo_redo_chain` | 50 | 1 | **2.0%** |

## RQ1 Temporal Depth Degradation Curve
**Failure Onset (L_T @ τ=0.70)**: `2`

| Depth (T) | Accuracy |
|---|---|
| T = 2 | 10.0% |
| T = 4 | 6.0% |
| T = 6 | 10.0% |
| T = 8 | 16.0% |
| T = 12 | 8.0% |
| T = 16 | 6.0% |

## RQ2 Revision Complexity Curve

| Depth (T) | Accuracy (V ≥ 2) |
|---|---|
| T = 4 | 2.0% |
| T = 8 | 14.0% |
| T = 12 | 0.0% |
| T = 16 | 0.0% |

## RQ3 Distractor Interference Curve
**Failure Onset (L_D @ τ=0.70)**: `4`

| Distractors (D) | Accuracy |
|---|---|
| D = 4 | 7.0% |
| D = 8 | 36.0% |
| D = 16 | 52.0% |
