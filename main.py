import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.ion()


file_path = "./file/AIWC-DATA-COLLECT.xlsx"
xls = pd.ExcelFile(file_path)

available_sheets = xls.sheet_names
print("Available Sheets:", available_sheets)

def brief_visual_summary(sheet_name, df):
    print(f"\n🔹 Processing Sheet: {sheet_name}")
    print(df.head(3))


    categorical_cols = [col for col in df.columns if df[col].dtype == "object" and df[col].nunique() < 10]
    numerical_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]

    plt.figure(figsize=(10, 5))

    if categorical_cols:
        col = categorical_cols[0]
        sns.countplot(y=col, data=df, order=df[col].value_counts().index, palette="viridis")
        plt.title(f"Distribution of {col} in {sheet_name}")
        plt.xlabel("Count")
        plt.ylabel(col)

    elif numerical_cols:
        col = numerical_cols[0]
        sns.histplot(df[col], kde=True, bins=20, color="blue")
        plt.title(f"Distribution of {col} in {sheet_name}")
        plt.xlabel(col)
        plt.ylabel("Frequency")

    plt.show(block=True)

for sheet in available_sheets:
    df = xls.parse(sheet)

    if df.empty:
        print(f"⚠️ Skipping {sheet} (Empty Sheet)")
        continue

    brief_visual_summary(sheet, df)

print("\n✅ Brief representations generated successfully!")
