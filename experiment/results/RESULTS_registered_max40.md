# Results — machine arm (exploratory)

**Reader models:** 12 · **item-administrations:** 529 parsed of 576 calls (compliance 91.8%, strict JSON 87.8%) · **errors:** 47

**Status: exploratory.** Per the pre-registration (§7) this arm is underpowered for the effect sizes of interest and issues no confirmatory verdict; it measures machine legibility, not comprehension.

**Compliance by completion budget** (the registered setting is `max_tokens=40`; deviation #1 re-runs one model's empty-content cells at 1024):

- `max_tokens=40`: 576 calls, 529 parsed, 47 errors

## Pre-registered quantities

| quantity | value |
|---|---|
| accuracy, formal | 0.932 (246/264) |
| accuracy, plain | 0.940 (249/265) |
| primary test: mean item difference (plain − formal) | +0.008 |
| primary test: exact sign-flip p (two-sided) | 0.5000 (exact) |
| 95% bootstrap CI on the mean item difference | [+0.000, +0.019] |
| logistic FE: beta (plain) | +0.808 (OR 2.24, Wald p 0.0099) |
| logistic FE: average marginal effect | +5.2 pp |
| TOST vs ±5 pp (SESOI) | equivalent (p_lo=0.0000, p_hi=0.0000) |
| reader-cluster bootstrap 95% CI on beta | [+0.480, +17.842] |

## Accuracy by language and register

| cell | accuracy | n |
|---|---|---|
| en|formal | 0.939 | 132 |
| en|plain | 0.947 | 132 |
| uk|formal | 0.924 | 132 |
| uk|plain | 0.932 | 133 |

## Accuracy by item type and register

| cell | accuracy | n |
|---|---|---|
| extraction|formal | 0.935 | 154 |
| extraction|plain | 0.948 | 155 |
| inference|formal | 0.927 | 110 |
| inference|plain | 0.927 | 110 |

## Secondary (pre-specified, machine arm = exploratory)

- register x language (uk): p = 0.5820, BH threshold 0.5820, reject = False
- register x item type (inference): p = 0.1885, BH threshold 0.3769, reject = False

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
| qwen/qwen3.5-9b | 1 | 1.000 | n/a | n/a |
| qwen/qwen-2.5-7b-instruct | 48 | 0.938 | +4.2 | +2.7 |
| meta-llama/llama-3.1-8b-instruct | 48 | 0.917 | +0.0 | +4.2 |
| meta-llama/llama-3.2-1b-instruct | 48 | 0.438 | +4.2 | -3.1 |

## Cost

| model | calls | prompt tok | completion tok | est. USD |
|---|---|---|---|---|
| deepseek/deepseek-chat-v3.1 | 48 | 10007 | 315 | 0.0028 |
| deepseek/deepseek-v3.2 | 48 | 9932 | 334 | 0.0027 |
| google/gemini-2.5-flash-lite | 48 | 8620 | 378 | 0.0010 |
| google/gemini-3.1-flash-lite | 48 | 8620 | 288 | 0.0026 |
| meta-llama/llama-3.1-8b-instruct | 48 | 9185 | 336 | 0.0005 |
| meta-llama/llama-3.2-1b-instruct | 48 | 9110 | 402 | 0.0003 |
| mistralai/ministral-8b-2512 | 48 | 9358 | 336 | 0.0015 |
| mistralai/mistral-nemo | 48 | 9312 | 336 | 0.0002 |
| mistralai/mistral-small-24b-instruct-2501 | 48 | 9358 | 336 | 0.0005 |
| qwen/qwen-2.5-7b-instruct | 48 | 10958 | 336 | 0.0012 |
| qwen/qwen3-30b-a3b-instruct-2507 | 48 | 10958 | 320 | 0.0006 |
| qwen/qwen3.5-9b | 48 | 9836 | 2456 | 0.0014 |
| **total** | | | | **0.0152** |

## Item-level differences (plain − formal, proportion correct)

| item | difference |
|---|---|
| D1-Q1 | +0.000 |
| D1-Q2 | +0.000 |
| D2-Q1 | +0.000 |
| D2-Q2 | +0.000 |
| D3-Q1 | +0.045 |
| D3-Q2 | +0.045 |
| D4-Q1 | +0.000 |
| D4-Q2 | +0.000 |
| D5-Q1 | +0.000 |
| D5-Q2 | +0.000 |
| D6-Q1 | +0.000 |
| D6-Q2 | +0.000 |
