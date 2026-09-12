# Evaluation Report: `qwen2.5-3b` on `full_benchmark`

- **Model ID**: `Qwen/Qwen2.5-3B-Instruct` (3.0B params)
- **Total Instances**: 1150
- **Overall Accuracy (A_final)**: **49.83%**
- **Runtime**: 4405.80s

## Trajectory Family Accuracies

| Trajectory Family | Instances | Correct | Accuracy |
|---|---|---|---|
| `basic_chain` | 300 | 293 | **97.7%** |
| `revision` | 200 | 43 | **21.5%** |
| `interleaved_chain` | 400 | 72 | **18.0%** |
| `split_chain` | 50 | 33 | **66.0%** |
| `merge_chain` | 50 | 46 | **92.0%** |
| `swap_chain` | 50 | 8 | **16.0%** |
| `undo_chain` | 50 | 46 | **92.0%** |
| `undo_redo_chain` | 50 | 32 | **64.0%** |

## RQ1 Temporal Depth Degradation Curve
**Failure Onset (L_T @ τ=0.70)**: `None`

| Depth (T) | Accuracy |
|---|---|
| T = 2 | 100.0% |
| T = 4 | 100.0% |
| T = 6 | 100.0% |
| T = 8 | 98.0% |
| T = 12 | 98.0% |
| T = 16 | 90.0% |

## RQ2 Revision Complexity Curve

| Depth (T) | Accuracy (V ≥ 2) |
|---|---|
| T = 4 | 6.0% |
| T = 8 | 76.0% |
| T = 12 | 2.0% |
| T = 16 | 2.0% |

## RQ3 Distractor Interference Curve
**Failure Onset (L_D @ τ=0.70)**: `4`

| Distractors (D) | Accuracy |
|---|---|
| D = 4 | 18.7% |
| D = 8 | 16.0% |
| D = 16 | 16.0% |
