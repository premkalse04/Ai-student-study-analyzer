def performance_level(score, attendance):
    if score >= 85 and attendance >= 85:
        return "🟢 Excellent"
    elif score >= 60 and attendance >= 70:
        return "🟡 Average"
    return "🔴 At Risk"


def generate_recommendation(study, sleep, attendance, assignment, score):
    return {
        "Performance": performance_level(score, attendance),
        "Study": "Increase study hours to 2–4 hrs/day." if study < 2 else "Good study routine.",
        "Sleep": "Sleep at least 7–8 hrs/day." if sleep < 7 else "Healthy sleep schedule.",
        "Attendance": "Improve attendance for better clarity." if attendance < 75 else "Attendance is good.",
        "Assignments": "Complete assignments regularly." if assignment < 80 else "Good assignment consistency.",
        "Advice": "Need Improvement" if score < 60 else "Maintain consistency and revise weekly."
    }
