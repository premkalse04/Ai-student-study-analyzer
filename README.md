<img width="1065" height="355" alt="image" src="https://github.com/user-attachments/assets/73c2e6d6-66e3-4a6b-b6e8-a2d1540431ea" />

🎓 StudyTrack – AI Study Habit Recommender System

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

StudyTrack is an AI-powered academic analytics platform designed to analyze student study habits, predict academic performance, and generate personalized learning recommendations using Machine Learning.

Built as a full-stack data-driven application, StudyTrack helps educators and students gain actionable insights from study behavior data such as study hours, sleep patterns, attendance, and assignment completion

## 🌟 Key Highlights

- AI-based prediction of academic performance  
- Personalized study, sleep, and attendance recommendations  
- Secure login & signup system  
- Interactive analytics dashboard  
- Individual and bulk prediction support  
- Clean, modern Streamlit UI  

---

## 🔐 Secure Authentication

- Login & Signup with encrypted passwords (SHA-256)
- Authentication activity logging (login & signup history)
- **Hidden Admin Access** (not visible in sidebar)
- SQLite-based user & authentication database

---

## 📁 Dataset Upload & Processing

- Upload **Excel (.xlsx)** or **CSV** datasets
- Automatic column mapping & normalization
- Data cleaning and validation
- Live preview of uploaded dataset
- Download cleaned dataset for prediction

---

## 🤖 Machine Learning Engine

- **Linear Regression** for academic score prediction
- **K-Means Clustering** for student segmentation
- Model evaluation using **R² Score** and **Mean Squared Error**
- Reusable trained model for bulk predictions

---

## 📊 Analytics Dashboard

- Actual vs Predicted score comparison
- Habit-based student clustering
- Performance distribution analysis
- Key insights & statistics
- Exportable **PDF analytics report**

---

## 🎯 Intelligent Recommendations

- Personalized study improvement tips
- Sleep and attendance optimization guidance
- Risk-level classification:
  - At Risk
  - Average
  - Excellent
- Supports both **individual** and **bulk** predictions

---

## 🛠️ Technology Stack

### Frontend
- Streamlit
- Custom modern UI with CSS

### Backend & Data
- Python
- SQLite (User & Auth History)

### Machine Learning
- Scikit-learn
- Pandas, NumPy
- Matplotlib
  
## 📁 Project Structure

```text
├── app.py                  # Main application
├── homepage.py             # Landing page
├── styles.py               # Global CSS styling
│
├── auth/
│   ├── auth_utils.py       # User & auth management
│   └── users.db            # SQLite database
│
├── auth_page.py            # Login / Signup UI
├── login.py
├── signup.py
│
├── excel_utils.py          # Dataset normalization
├── recommendation.py      # Recommendation engine
├── analysis_charts.py      # Visualizations
├── pdf_utils.py            # PDF export
│
└── README.md
---

📊 Dataset Requirements

Your training dataset should include the following fields
(common aliases are handled automatically):

Required Columns
Study_Hours_Per_Day
Sleep_Hours
Attendance_Percentage
Assignment_Completion
Social_Media_Hours
Exercise_Hours
Test_Score


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/premkalse04/Ai-student-study-analyzer.git
cd Ai-student-study-analyzer

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py


🧠 Machine Learning Workflow

- Upload training dataset
- Clean & normalize data
- Train regression model
- Evaluate model performance
- Predict student scores
- Segment students using clustering
- Generate personalized recommendations

🎓 Academic Context

This project was developed as a Final Year Engineering Project to demonstrate:

1.Real-world Machine Learning implementation

2.Secure authentication systems

3.End-to-end data analytics pipeline

4.Full-stack application development



👨‍💻 Author

Prem Kalse
Final Year Engineering Student

Guided by:
Mr. Anil Kumar


📜 License
This project is intended for academic and educational purposes.
You are free to fork and extend it for learning and research.
