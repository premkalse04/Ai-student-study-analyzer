# ------------------------------------------------------------
# study_habit_eda_clean_final.py
# Complete cleaning + EDA pipeline using Pandas, NumPy, Seaborn, Matplotlib
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# 1️⃣ Load Data
# ------------------------------------------------------------
def load_data(file_path):
    df = pd.read_excel(file_path)
    print(" Data Loaded Successfully!\n")
    print("Initial Columns:\n", df.columns.tolist())
    print("\nFirst 5 Rows:\n", df.head(), "\n")
    return df

# ------------------------------------------------------------
# 2️⃣ Clean Data
# ------------------------------------------------------------
def clean_data(df):
    print(" Step 1: Shape Before Cleaning:", df.shape)

    # Drop completely empty columns
    df.dropna(axis=1, how='all', inplace=True)

    # Remove duplicated columns (keep the first one)
    df = df.loc[:, ~df.columns.duplicated()]

    # Drop unnecessary columns manually (if names known)
    unnecessary = ['Random Notes', 'Extra_Column', 'Empty1']
    df.drop(columns=[col for col in unnecessary if col in df.columns], inplace=True, errors='ignore')

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Fill numeric NaN values with mean
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Rename columns for simplicity
    rename_map = {
        'Study Hours/Day': 'StudyHours',
        'Sleep Hours': 'SleepHours',
        'Social Media Hours': 'SocialMedia',
        'Exercise Hours': 'Exercise',
        'Attention Level (1-10)': 'AttentionLevel'
    }
    df.rename(columns=rename_map, inplace=True)

    print("\n Step 2: Columns After Cleaning:\n", df.columns.tolist())
    print(" Shape After Cleaning:", df.shape)
    print("\nCleaned Data (first 5 rows):\n", df.head())
    return df

# ------------------------------------------------------------
# 3️⃣ EDA (Exploratory Data Analysis)
# ------------------------------------------------------------
def perform_eda(df):
    print("\n Basic Dataset Info:")
    print(df.info())

    print("\n Descriptive Statistics:\n", df.describe())

    print("\n Checking Missing Values:\n", df.isnull().sum())

    print("\n Correlation Matrix:\n", df.corr(numeric_only=True))

    # NumPy insights
    study = np.array(df['StudyHours'])
    attention = np.array(df['AttentionLevel'])
    cov = np.cov(study, attention)[0, 1]
    print(f"\n Covariance (StudyHours vs AttentionLevel): {cov:.2f}")

# ------------------------------------------------------------
# 4️⃣ Visualizations (Seaborn + Matplotlib)
# ------------------------------------------------------------
def visualize_data(df):
    print("\n Creating Visuals...")

    # Histogram of study hours
    plt.figure(figsize=(7,5))
    plt.hist(df['StudyHours'], bins=5, color='skyblue', edgecolor='black')
    plt.title('Distribution of Study Hours per Day')
    plt.xlabel('Study Hours')
    plt.ylabel('Number of Students')
    plt.show()

    # Pairplot
    sns.pairplot(df[['StudyHours', 'SleepHours', 'SocialMedia', 'Exercise', 'AttentionLevel']], diag_kind='kde')
    plt.suptitle('Pairwise Relationships', y=1.02)
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(6,4))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()

# ------------------------------------------------------------
# 5️⃣ Main Function
# ------------------------------------------------------------
def main():
    file_path = 'rawdata.xlsx'
    df = load_data(file_path)
    df = clean_data(df)
    perform_eda(df)
    visualize_data(df)

    # Save cleaned dataset
    df.to_excel(r'Final Output\student_study_data_cleaned.xlsx', index=False)
    print("\n Cleaned data saved to 'student_study_data_cleaned.xlsx'")

# ------------------------------------------------------------
if __name__ == "__main__":
    main()