import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_data(df):
    df = df.copy()

    features = [
        'Study_Hours_Per_Day',
        'Sleep_Hours',
        'Attendance_Percentage',
        'Assignment_Completion',
        'Final_Grade'
    ]

    X = df[features].apply(pd.to_numeric, errors='coerce').dropna()
    original_index = X.index

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)

    df.loc[original_index, 'cluster'] = cluster_labels

    cluster_means = (
        df.loc[original_index]
        .groupby('cluster')['Final_Grade']
        .mean()
        .sort_values(ascending=False)
    )

    labels = ['High Performer', 'Good Performer', 'Average Performer', 'Needs Improvement']
    label_map = dict(zip(cluster_means.index, labels))

    df.loc[original_index, 'performance_label'] = df.loc[original_index, 'cluster'].map(label_map)

    return df


def main():
    df = pd.read_excel(
        r"p:\Ai-Student Study Analyzer\Milstone1\cleaned_data_visual.xlsx"
    )

    df_clustered = cluster_data(df)

    df_clustered.to_csv(
        r"p:\Ai-Student Study Analyzer\Milstone1\clustered_data.csv",
        index=False
    )

    print("✅ Clustering completed successfully")

if __name__ == "__main__":
    main()
