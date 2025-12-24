import pandas as pd
from recommendation import generate_recommendation, performance_level

# Canonical column mapping
COLUMN_ALIASES = {
    "study_hours_per_day": ["study_hours_per_day", "study_hours", "studyhours"],
    "sleep_hours": ["sleep_hours", "sleep"],
    "attendance_percentage": ["attendance_percentage", "attendance"],
    "assignment_completion": [
        "assignment_completion",
        "assignments_completed",
        "assignment_completed",
        "assignments_completion"
    ],
    "test_score": ["test_score", "score", "exam_score"]
}

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def map_columns(df: pd.DataFrame) -> pd.DataFrame:
    mapped = {}

    for standard_col, aliases in COLUMN_ALIASES.items():
        for col in df.columns:
            if col in aliases:
                mapped[col] = standard_col
                break

    df = df.rename(columns=mapped)

    missing = [col for col in COLUMN_ALIASES if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {', '.join(missing)}")

    return df


def process_excel(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)
    df = map_columns(df)

    def compute(row):
        rec = generate_recommendation(
            row["study_hours_per_day"],
            row["sleep_hours"],
            row["attendance_percentage"],
            row["assignment_completion"],
            row["test_score"],
        )
        perf = rec.get("Performance")
        return pd.Series(
            {
                "Performance_Level": perf,
                "Rec_Study": rec.get("Study"),
                "Rec_Sleep": rec.get("Sleep"),
                "Rec_Attendance": rec.get("Attendance"),
                "Rec_Assignments": rec.get("Assignments"),
                "Rec_Advice": rec.get("Advice"),
                "Rec_Summary": f"{perf} • {rec.get('Study')} | {rec.get('Sleep')} | "
                               f"{rec.get('Attendance')} | {rec.get('Assignments')} | {rec.get('Advice')}",
            }
        )

    rec_df = df.apply(compute, axis=1)
    df = pd.concat([df, rec_df], axis=1)

    return df
