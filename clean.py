"""
clean.py — Data Cleaning Script
Part of: skill-data-cleaning
"""

import pandas as pd
import numpy as np
import argparse
import os

def inspect_data(df):
    print("\n📊 DATASET INSPECTION")
    print(f"{'='*45}")
    print(f"Shape:        {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"Duplicates:   {df.duplicated().sum()}")
    print(f"\nMissing Values:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(1)
    for col in df.columns:
        if missing[col] > 0:
            print(f"  {col:<25} {missing[col]} ({missing_pct[col]}%)")
    print(f"\nColumn Types:")
    for col, dtype in df.dtypes.items():
        print(f"  {col:<25} {dtype}")
    print(f"{'='*45}\n")

def detect_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[col] < lower) | (df[col] > upper)].index

def clean_data(df):
    report = []
    original_shape = df.shape

    # 1. Standardize column names
    df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]
    report.append("✅ Column names standardized (lowercase + underscores)")

    # 2. Drop high-missing columns
    missing_pct = df.isnull().sum() / len(df)
    high_missing = missing_pct[missing_pct > 0.6].index.tolist()
    if high_missing:
        df.drop(columns=high_missing, inplace=True)
        report.append(f"🗑️  Dropped {len(high_missing)} column(s) with >60% missing: {high_missing}")

    # 3. Remove duplicates
    dupes = df.duplicated().sum()
    if dupes > 0:
        df.drop_duplicates(inplace=True)
        report.append(f"🗑️  Removed {dupes} duplicate row(s)")

    # 4. Fill missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['str', 'object']).columns

    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            report.append(f"🔧 Filled missing in '{col}' with median ({median_val:.2f})")

    for col in categorical_cols:
        if df[col].isnull().sum() > 0:
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)
            report.append(f"🔧 Filled missing in '{col}' with mode ('{mode_val}')")

    # 5. Flag outliers
    outlier_summary = []
    for col in numeric_cols:
        outlier_idx = detect_outliers(df, col)
        if len(outlier_idx) > 0:
            df.loc[outlier_idx, f"{col}_outlier_flag"] = True
            df[f"{col}_outlier_flag"] = df[f"{col}_outlier_flag"].fillna(False)
            outlier_summary.append(f"'{col}': {len(outlier_idx)} outliers flagged")

    if outlier_summary:
        report.append(f"🚩 Outliers flagged (not removed): {', '.join(outlier_summary)}")

    final_shape = df.shape
    report.append(f"\n📈 SUMMARY: {original_shape[0]} → {final_shape[0]} rows | "
                  f"{original_shape[1]} → {final_shape[1]} columns")

    return df, report


def main():
    parser = argparse.ArgumentParser(description="Data Cleaning Skill")
    parser.add_argument("--input",   required=True, help="Input CSV file")
    parser.add_argument("--output",  default="cleaned.csv", help="Output CSV file")
    parser.add_argument("--inspect", action="store_true", help="Inspect only, no cleaning")
    args = parser.parse_args()

    print(f"\n🧹 Loading: {args.input}")
    df = pd.read_csv(args.input)

    if args.inspect:
        inspect_data(df)
        return

    inspect_data(df)
    print("🔧 Cleaning in progress...\n")

    df_clean, report = clean_data(df)

    # Save output
    df_clean.to_csv(args.output, index=False)

    # Save report
    report_path = args.output.replace(".csv", "_report.txt")
    with open(report_path, "w") as f:
        f.write("DATA CLEANING REPORT\n")
        f.write("="*45 + "\n")
        f.write(f"Input:  {args.input}\n")
        f.write(f"Output: {args.output}\n\n")
        f.write("Changes Made:\n")
        for line in report:
            f.write(f"  {line}\n")

    print("CLEANING REPORT:")
    for line in report:
        print(f"  {line}")
    print(f"\n✅ Saved: {args.output}")
    print(f"📄 Report: {report_path}\n")


if __name__ == "__main__":
    main()
