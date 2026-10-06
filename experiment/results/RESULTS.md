# Results — machine arm (exploratory)

**Reader models:** 12 · **item-administrations:** 860 parsed of 864 calls (compliance 99.5%, strict JSON 95.1%) · **errors:** 4

**Status: exploratory.** Per the pre-registration (§7) this arm is underpowered for the effect sizes of interest and issues no confirmatory verdict; it measures machine legibility, not comprehension.

**Compliance by completion budget** (the registered setting is `max_tokens=40`; deviation #1 re-runs one model's empty-content cells at 1024):

- `max_tokens=40`: 864 calls, 795 parsed, 69 errors
- `max_tokens=1024`: 70 calls, 65 parsed, 5 errors

## Pre-registered quantities

| quantity | value |
|---|---|
| accuracy, formal | 0.928 (398/429) |
| accuracy, plain | 0.926 (399/431) |
| primary test: mean item difference (plain − formal) | -0.002 |
| primary test: exact sign-flip p (two-sided) | 1.0000 (sampled) |
| 95% bootstrap CI on the mean item difference | [-0.018, +0.012] |
| logistic FE: beta (plain) | +0.618 (OR 1.86, Wald p 0.0090) |
| logistic FE: average marginal effect | +4.5 pp |
| TOST vs ±10 pp (SESOI) | equivalent (p_lo=0.0000, p_hi=0.0000) |
| reader-cluster bootstrap 95% CI on beta | [+0.443, +1.576] |

## Accuracy by language and register

| cell | accuracy | n |
|---|---|---|
| en|formal | 0.935 | 214 |
| en|plain | 0.930 | 215 |
| uk|formal | 0.921 | 215 |
| uk|plain | 0.921 | 216 |

## Accuracy by item type and register

| cell | accuracy | n |
|---|---|---|
| extraction|formal | 0.948 | 191 |
| extraction|plain | 0.948 | 192 |
| inference|formal | 0.912 | 238 |
| inference|plain | 0.908 | 239 |

## Secondary (pre-specified, machine arm = exploratory)

- register x language (uk): p = 0.6995, BH threshold 0.6995, reject = False
- register x item type (inference): p = 0.1409, BH threshold 0.2818, reject = False

## Per model

| model | n | accuracy | item diff (pp) | logistic AME (pp) |
|---|---|---|---|---|
| deepseek/deepseek-chat-v3.1 | 72 | 1.000 | +0.0 | +2.8 |
| deepseek/deepseek-v3.2 | 72 | 1.000 | +0.0 | +2.8 |
| google/gemini-2.5-flash-lite | 72 | 1.000 | +0.0 | +2.8 |
| google/gemini-3.1-flash-lite | 72 | 1.000 | +0.0 | +2.8 |
| qwen/qwen3-30b-a3b-instruct-2507 | 72 | 1.000 | +0.0 | +2.8 |
| qwen/qwen3.5-9b | 68 | 1.000 | +0.0 | +2.9 |
| mistralai/mistral-small-24b-instruct-2501 | 72 | 0.986 | -2.8 | +1.8 |
| mistralai/ministral-8b-2512 | 72 | 0.944 | +0.0 | +2.8 |
| mistralai/mistral-nemo | 72 | 0.944 | +0.0 | +2.8 |
| qwen/qwen-2.5-7b-instruct | 72 | 0.944 | +0.0 | +4.4 |
| meta-llama/llama-3.1-8b-instruct | 72 | 0.889 | +0.0 | +4.2 |
| meta-llama/llama-3.2-1b-instruct | 72 | 0.417 | +0.0 | +4.7 |

## Cost

| model | calls | prompt tok | completion tok | est. USD |
|---|---|---|---|---|
| deepseek/deepseek-chat-v3.1 | 72 | 15550 | 473 | 0.0043 |
| deepseek/deepseek-v3.2 | 72 | 15441 | 500 | 0.0045 |
| google/gemini-2.5-flash-lite | 72 | 13474 | 557 | 0.0016 |
| google/gemini-3.1-flash-lite | 72 | 13474 | 432 | 0.0040 |
| meta-llama/llama-3.1-8b-instruct | 72 | 14264 | 504 | 0.0008 |
| meta-llama/llama-3.2-1b-instruct | 72 | 14132 | 617 | 0.0005 |
| mistralai/ministral-8b-2512 | 72 | 14609 | 504 | 0.0023 |
| mistralai/mistral-nemo | 72 | 14541 | 504 | 0.0003 |
| mistralai/mistral-small-24b-instruct-2501 | 72 | 14609 | 504 | 0.0008 |
| qwen/qwen-2.5-7b-instruct | 72 | 17083 | 504 | 0.0018 |
| qwen/qwen3-30b-a3b-instruct-2507 | 72 | 17083 | 478 | 0.0019 |
| qwen/qwen3.5-9b | 72 | 15304 | 47534 | 0.0087 |
| **total** | | | | **0.0314** |

## Item-level differences (plain − formal, proportion correct)

| item | difference |
|---|---|
| D1-Q1 | +0.000 |
| D1-Q2 | +0.000 |
| D1-Q3 | +0.005 |
| D2-Q1 | +0.000 |
| D2-Q2 | +0.000 |
| D2-Q3 | -0.083 |
| D3-Q1 | +0.043 |
| D3-Q2 | +0.042 |
| D3-Q3 | +0.042 |
| D4-Q1 | +0.000 |
| D4-Q2 | +0.000 |
| D4-Q3 | +0.000 |
| D5-Q1 | +0.000 |
| D5-Q2 | +0.000 |
| D5-Q3 | -0.083 |
| D6-Q1 | +0.000 |
| D6-Q2 | +0.000 |
| D6-Q3 | +0.000 |
