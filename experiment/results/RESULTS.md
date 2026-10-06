# Results — machine arm (exploratory)

**Reader models:** 12 · **item-administrations:** 575 parsed of 576 calls (compliance 99.8%, strict JSON 95.8%) · **errors:** 1

**Status: exploratory.** Per the pre-registration (§7) this arm is underpowered for the effect sizes of interest and issues no confirmatory verdict; it measures machine legibility, not comprehension.

**Compliance by completion budget** (the registered setting is `max_tokens=40`; deviation #1 re-runs one model's empty-content cells at 1024):

- `max_tokens=40`: 576 calls, 529 parsed, 47 errors
- `max_tokens=1024`: 47 calls, 46 parsed, 1 errors

## Pre-registered quantities

| quantity | value |
|---|---|
| accuracy, formal | 0.937 (269/287) |
| accuracy, plain | 0.944 (272/288) |
| primary test: mean item difference (plain − formal) | +0.007 |
| primary test: exact sign-flip p (two-sided) | 0.5000 (exact) |
| 95% bootstrap CI on the mean item difference | [+0.000, +0.018] |
| logistic FE: beta (plain) | +0.862 (OR 2.37, Wald p 0.0053) |
| logistic FE: average marginal effect | +5.3 pp |
| TOST vs ±10 pp (SESOI) | equivalent (p_lo=0.0000, p_hi=0.0000) |
| reader-cluster bootstrap 95% CI on beta | [+0.509, +18.014] |

## Accuracy by language and register

| cell | accuracy | n |
|---|---|---|
| en|formal | 0.944 | 144 |
| en|plain | 0.951 | 144 |
| uk|formal | 0.930 | 143 |
| uk|plain | 0.938 | 144 |

## Accuracy by item type and register

| cell | accuracy | n |
|---|---|---|
| extraction|formal | 0.940 | 167 |
| extraction|plain | 0.952 | 168 |
| inference|formal | 0.933 | 120 |
| inference|plain | 0.933 | 120 |

## Secondary (pre-specified, machine arm = exploratory)

- register x language (uk): p = 0.5834, BH threshold 0.5834, reject = False
- register x item type (inference): p = 0.1479, BH threshold 0.2957, reject = False

## Per model

| model | n | accuracy | item diff (pp) | logistic AME (pp) |
|---|---|---|---|---|
| deepseek/deepseek-chat-v3.1 | 48 | 1.000 | +0.0 | +4.2 |
| deepseek/deepseek-v3.2 | 48 | 1.000 | +0.0 | +4.2 |
| google/gemini-2.5-flash-lite | 48 | 1.000 | +0.0 | +4.2 |
| google/gemini-3.1-flash-lite | 48 | 1.000 | +0.0 | +4.2 |
| mistralai/ministral-8b-2512 | 48 | 1.000 | +0.0 | +4.2 |
| mistralai/mistral-nemo | 48 | 1.000 | +0.0 | +4.2 |
| mistralai/mistral-small-24b-instruct-2501 | 48 | 1.000 | +0.0 | +4.2 |
| qwen/qwen3-30b-a3b-instruct-2507 | 48 | 1.000 | +0.0 | +4.2 |
| qwen/qwen3.5-9b | 47 | 1.000 | +0.0 | +4.3 |
| qwen/qwen-2.5-7b-instruct | 48 | 0.938 | +4.2 | +2.7 |
| meta-llama/llama-3.1-8b-instruct | 48 | 0.917 | +0.0 | +4.2 |
| meta-llama/llama-3.2-1b-instruct | 48 | 0.438 | +4.2 | -3.1 |

## Cost

| model | calls | prompt tok | completion tok | est. USD |
|---|---|---|---|---|
| deepseek/deepseek-chat-v3.1 | 48 | 10007 | 315 | 0.0028 |
| deepseek/deepseek-v3.2 | 48 | 9932 | 334 | 0.0029 |
| google/gemini-2.5-flash-lite | 48 | 8620 | 378 | 0.0010 |
| google/gemini-3.1-flash-lite | 48 | 8620 | 288 | 0.0026 |
| meta-llama/llama-3.1-8b-instruct | 48 | 9185 | 336 | 0.0005 |
| meta-llama/llama-3.2-1b-instruct | 48 | 9110 | 402 | 0.0003 |
| mistralai/ministral-8b-2512 | 48 | 9358 | 336 | 0.0015 |
| mistralai/mistral-nemo | 48 | 9312 | 336 | 0.0002 |
| mistralai/mistral-small-24b-instruct-2501 | 48 | 9358 | 336 | 0.0005 |
| qwen/qwen-2.5-7b-instruct | 48 | 10958 | 336 | 0.0012 |
| qwen/qwen3-30b-a3b-instruct-2507 | 48 | 10958 | 320 | 0.0012 |
| qwen/qwen3.5-9b | 48 | 9836 | 28258 | 0.0052 |
| **total** | | | | **0.0198** |

## Item-level differences (plain − formal, proportion correct)

| item | difference |
|---|---|
| D1-Q1 | +0.000 |
| D1-Q2 | +0.000 |
| D2-Q1 | +0.000 |
| D2-Q2 | +0.000 |
| D3-Q1 | +0.043 |
| D3-Q2 | +0.042 |
| D4-Q1 | +0.000 |
| D4-Q2 | +0.000 |
| D5-Q1 | +0.000 |
| D5-Q2 | +0.000 |
| D6-Q1 | +0.000 |
| D6-Q2 | +0.000 |
