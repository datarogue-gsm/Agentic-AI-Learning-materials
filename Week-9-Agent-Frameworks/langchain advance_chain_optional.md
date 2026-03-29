# Use Case 1: Multi-format Data Extraction

---

## What this is

This example shows how to take a messy job description and turn it into clean, structured data (JSON).

Instead of manually reading and parsing text, we let the LLM handle extraction, then clean it up in steps.

---

## Why this matters

Job descriptions are usually:

* not structured
* written differently every time
* hard to store or query

If we convert them into JSON:

* we can store them in a database
* filter/search easily
* run analytics

---

## How it works

```text
Job Description
    ↓
Extraction (LLM)
    ↓
Validation
    ↓
JSON Parsing
    ↓
Structured Output
```

---

## Steps involved

### 1. Extraction

We ask the model to pull out fields like:

* company name
* position
* requirements
* benefits
* contact info

---

### 2. Validation

The first output is not always perfect.

So we run a second step to:

* fix formatting
* fill missing fields
* clean things up

---

### 3. JSON Parsing

LLMs sometimes return broken JSON.

So we:

* try parsing
* if it fails → fallback to default structure

---

### 4. Formatting (optional)

We can also convert the JSON into a clean job posting format.

---

## Key idea

Don’t rely on a single LLM call.

Break it into steps:

```text
Extract → Clean → Parse → Format
```

---

## Common issues

* JSON not valid
* Missing fields
* Extra text in response

That’s why validation + fallback is important.

---

## Where this can be used

* Job portals
* Resume parsing
* HR systems
* Any unstructured → structured conversion

---

## Quick takeaway

LLMs are good at extracting info,
but you still need structure around them to make things reliable.

---

---

# Use Case 2: Batch Processing with LLMs

---

## What this is

This shows how to process **multiple inputs (like reviews)** efficiently instead of one at a time.

---

## Why this matters

In real systems, you don’t get one input — you get thousands.

Processing them one by one:

* slow
* expensive
* not scalable

---

## Idea

We process reviews in a loop, and for each review:

* extract sentiment
* extract aspects
* generate summary

---

## Flow

```text
Multiple Reviews
      ↓
Loop
      ↓
Parallel analysis (per review)
      ↓
Store results
```

---

## What’s happening inside

### Per review:

We run multiple tasks at the same time:

* sentiment
* aspects
* summary

(using `RunnableParallel`)

---

### Across reviews:

We loop through all reviews:

```python
for review in reviews:
```

---

## Why this is efficient

Instead of:

```text
Do everything step by step ❌
```

We do:

```text
Parallel tasks per item + loop over items ✅
```

---

## Small additions that help

* progress tracking (`tqdm`)
* error handling (skip failed ones)

---

## Key idea

Two levels of efficiency:

1. Parallel work per item
2. Batch processing across items

---

## Where this is useful

* review analysis
* support tickets
* feedback processing
* log analysis

---

## Things to avoid

* deeply nested LLM calls
* no error handling
* unclear pipeline structure

---

## Quick takeaway

Batch processing is not just looping —
it’s about structuring work so it scales.

---
