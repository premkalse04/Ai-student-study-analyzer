import matplotlib.pyplot as plt
import pandas as pd

def plot_actual_vs_predicted(y_test, y_pred):
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.set_xlabel("Actual Score")
    ax.set_ylabel("Predicted Score")
    ax.set_title("Actual vs Predicted Scores")
    ax.grid(True)
    return fig

def plot_clusters(df):
    fig, ax = plt.subplots()
    for cluster in df['Cluster_Number'].unique():
        data = df[df['Cluster_Number'] == cluster]
        ax.scatter(
            data['Study_Hours_Per_Day'],
            data['Test_Score'],
            label=f"Cluster {cluster}"
        )
    ax.set_title("Student Clustering")
    ax.set_xlabel("Study Hours / Day")
    ax.set_ylabel("Test Score")
    ax.legend()
    ax.grid(True)
    return fig

def cluster_summary(df):
    return df.groupby("Cluster_Number").agg({
        "Test_Score": "mean",
        "Study_Hours_Per_Day": "mean",
        "Attendance_Percentage": "mean"
    }).round(2)

