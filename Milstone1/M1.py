import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_data(df):
    df = df.copy()

    features = [
        'study Hours/day',
        'sleep_hours',
        'attendance_percentage',
        'assignments_completed',
        'final_grade'
    ]

    X = df[features].apply(pd.to_numeric, errors='coerce')
    X = X.dropna()

    original_index = X.index

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=4, random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)

    clustered = df.loc[original_index].copy()
    clustered['cluster'] = cluster_labels

    cluster_means = clustered.groupby('cluster')['final_grade'].mean().sort_values(ascending=False)
    performance_labels = ['high performer', 'good performer', 'average performer', 'need improvement']

    cluster_label_map = {cluster: performance_labels[i] for i, cluster in enumerate(cluster_means.index)}

    clustered['performance_label'] = clustered['cluster'].map(cluster_label_map)

    result_df = df.copy()
    result_df.loc[original_index, 'cluster'] = clustered['cluster']
    result_df.loc[original_index, 'performance_label'] = clustered['performance_label']

    print(result_df[['cluster', 'performance_label']].value_counts())
    return result_df


def main():
    # Load Excel file instead of using cleaning_eda
    df = pd.read_excel('cleaned_data_visual.xlsx')

    df_clustered = cluster_data(df)

    df_clustered.to_csv(r'N:\ISI6.0\clustered_data.csv', index=False)

if __name__ == "__main__":
    main()
