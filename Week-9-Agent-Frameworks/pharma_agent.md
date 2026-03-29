# Pharmaceutical Research Assistant Agent

---

## What this is

This is a simple agent built using LangChain that acts like a basic pharmaceutical assistant.

It can:

* Look up drug information
* Check safety (contraindications)
* Calculate dosage
* Fetch additional medical context (simulated)

The idea is to show how an agent can **choose the right tool based on the question**.

---

## Why this matters

In real-world pharma or healthcare systems, a lot of tasks are:

* repetitive
* rule-based
* safety-critical

This kind of setup helps:

* reduce manual effort
* make responses more structured
* avoid random or unsafe answers

---

## How it works (high level)

```text
User question
   ↓
Agent understands intent
   ↓
Picks the right tool
   ↓
Runs the tool
   ↓
Returns answer
```

---

## Tools used

* `lookup_drug` → basic drug info
* `safety_check` → contraindications
* `dosage_calculator` → dose calculation
* `external_medical_search` → fallback for extra info

Each tool does one job. The agent decides which one to use.

---

## Example

**Input:**

```
Calculate dosage for a 70kg patient at 10 mg/kg
```

**What happens:**

* Agent detects it's a dosage problem
* Calls `dosage_calculator`
* Returns result

---

## What’s interesting here

* The model is not doing everything
* It mostly decides *which tool to call*
* Tools handle the actual logic

That’s the core idea behind agentic systems.

---

## Things to keep in mind

* Keep tools simple and focused
* Don’t overlap tool responsibilities too much
* Always guide the agent with a clear prompt
* In sensitive domains (like pharma), avoid guessing

---

## Where this can go next

* Connect to real medical APIs
* Add patient history context
* Chain multiple tools (carefully)
* Add logging / validation layers

---

## Final thought

This is a small setup, but the pattern is useful.

Once you understand this, you can build:

* support assistants
* research tools
* internal automation systems

---
