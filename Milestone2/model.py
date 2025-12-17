import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ---------- LOAD ----------
df = pd.read_excel('data4.xlsx')
print(df.head())

# ---------- REGRESSION ----------
X = df[['Study_Hours_Per_Day','Sleep_Hours','Attendance_Percentage']]
Y = df['Test_Score']   # FIXED: your sheet contains Test_Score, not Exam_Score

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(Y_test, Y_pred))
print("R^2 Score:", r2_score(Y_test, Y_pred))

# ---------- NEW PREDICTION ----------
new_Student = pd.DataFrame({
    'Study_Hours_Per_Day': [5],
    'Sleep_Hours': [7],
    'Attendance_Percentage': [90]
})
pred = model.predict(new_Student)
print("\nPredicted Score:", pred[0])

# ---------- PLOT ----------
plt.figure(figsize=(10,6))
plt.scatter(Y_test, Y_pred, color='red', s=120, label="Data Points", zorder=3)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='blue', linewidth=2, label="Perfect Prediction Line", zorder=1)
plt.xlabel('Actual Exam Scores')
plt.ylabel('Predicted Exam Scores')
plt.title('Actual vs Predicted Exam Scores')
plt.grid(True)
plt.legend()
plt.show()

