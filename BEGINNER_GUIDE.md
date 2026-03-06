# 🟢 Beginner Guide — No Coding Required

Welcome! You don't need to write a single line of code to use DS Agent Skills.

Here's exactly how to get started in 5 minutes.

---

## What you need

- Any AI assistant: Claude, ChatGPT, Gemini, or similar
- A dataset you want to analyze (CSV file works great)
- That's it.

---

## Step 1 — Open a skill file

Go into any skill folder and open the `SKILL.md` file.
Read it — it's written in plain language, not code.

Example: open `skill-data-cleaning/SKILL.md`

---

## Step 2 — Copy and paste into your AI

Open your AI assistant and write something like this:

```
I have a dataset I want to clean. 
Here are the instructions I want you to follow:

[paste the contents of SKILL.md here]

My data file is attached. Please follow the skill instructions.
```

Then attach your CSV file.

---

## Step 3 — Let the AI do the work

The AI reads the skill instructions and:
- Tells you what problems it found in your data
- Asks you to confirm before making big changes
- Delivers a clean file and a plain-language report

No code. No terminal. No setup.

---

## Real Example

**You upload:** `sales_january.csv` (messy, 500 rows, lots of missing values)

**You say:**
```
Read the skill instructions below and clean my sales file.
Tell me what you find before making changes.

[paste skill-data-cleaning/SKILL.md]
```

**AI responds:**
```
I found the following issues in your file:
- 47 missing values in "Revenue" column
- 12 duplicate rows
- 1 column ("Notes") is 90% empty

Should I proceed with cleaning? I'll fill missing Revenue 
with the median value and remove duplicates.
```

**You say:** Yes

**AI delivers:** Clean file + a simple report of what changed.

---

## Which skill should I start with?

| If you want to... | Use this skill |
|---|---|
| Fix a messy dataset | `skill-data-cleaning` |
| Understand your data better | `skill-eda` |
| Build a prediction model | `skill-ml-pipeline` |
| Explain results to your manager | `skill-report-generator` |

---

## Questions?

Join the community on Facebook → [Link to your group]
Post your question — someone will help within 24 hours.

---

*You don't need to be a data scientist to use data science.*
*You just need the right skill file.*
