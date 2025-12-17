import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ---------- LOAD ----------
df = pd.read_excel('data4.xlsx')

# ---------- FEATURES ----------
X = df[['Study_Hours_Per_Day','Sleep_Hours','Attendance_Percentage']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------- KMEANS ----------
kmeans = KMeans(n_clusters=3, random_state=42)  # FIXED: do not overwrite KMeans class
df['Cluster_Number'] = kmeans.fit_predict(X_scaled)

# ---------- REMARKS ----------
remarks = {
    0: "OK Performance! Can Improve",
    1: "Bad Performance! Needs Improvement",
    2: "Excellent Performance! Keep it up"
}
df['Remarks'] = df['Cluster_Number'].map(remarks)

print(df[['Study_Hours_Per_Day','Sleep_Hours','Attendance_Percentage','Cluster_Number','Remarks']].head())

df.to_excel('clustered_students_output.xlsx', index=False)

print("\nThree Clusters created and data saved to 'clustered_students.xlsx'")

# ---------- PLOT ----------
plt.figure(figsize=(10,6))

clusters = df['Cluster_Number'].unique()

for cluster in clusters:
    cluster_data = df[df['Cluster_Number'] == cluster]
    plt.scatter(
        cluster_data['Study_Hours_Per_Day'],
        cluster_data['Test_Score'],
        s=80,
        label=f"Cluster {cluster}"
    )

plt.xlabel("Study Hours Per Day")
plt.ylabel("Test Score")
plt.title("KMeans Clustering of Students (3 Clusters)")
plt.legend(title="Clusters")   
plt.grid(True)
plt.show()
