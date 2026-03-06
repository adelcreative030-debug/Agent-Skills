---
name: data-cleaning
description: >
  Use this skill whenever the user provides a raw dataset that needs cleaning.
  Triggers on: missing values, duplicate rows, inconsistent formats, outlier detection,
  column type errors, or any request to "clean", "prepare", or "fix" a dataset.
  Always use this before any analysis or modeling skill.
---

# Data Cleaning Skill

## What it does
Automatically detects and fixes the most common data quality issues
in any CSV or Excel dataset — missing values, duplicates, outliers,
and inconsistent formatting.

---

## When to use
- User uploads a raw dataset
- User says: "clean this", "fix this data", "prepare this for analysis"
- Before running `skill-eda` or `skill-ml-pipeline`

---

## Steps

### 1. Load & Inspect
```bash
python scripts/clean.py --input <file> --inspect
```
Outputs: shape, dtypes, missing value counts, duplicate count.

### 2. Auto-Clean
```bash
python scripts/clean.py --input <file> --output cleaned.csv
```
Applies:
- Drop columns with >60% missing values
- Fill numeric missing values with median
- Fill categorical missing values with mode
- Remove duplicate rows
- Standardize column names (lowercase, underscores)
- Detect and flag outliers (IQR method)

### 3. Review & Confirm
Show the user a before/after summary.
Ask: "Do you want to drop the outliers or keep them flagged?"

---

## Output
- `cleaned.csv` — clean dataset ready for analysis
- `cleaning_report.txt` — what was changed and why

---

## Important Rules
- Never drop a column without telling the user first
- Always show before/after row counts
- If more than 40% of rows are affected — warn the user before proceeding
- Preserve original file — always write to a new file

---

## Example
```
Input:  sales_data.csv (1200 rows, 8 columns, 23% missing)
Output: sales_data_cleaned.csv (1156 rows, 7 columns, 0% missing)
Report: 44 rows removed (duplicates + extreme outliers), 1 column dropped (>60% empty)
```
