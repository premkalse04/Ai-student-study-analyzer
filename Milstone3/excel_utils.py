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

    df["Performance_Level"] = df.apply(
        lambda r: performance_level(
            r["test_score"], r["attendance_percentage"]
        ),
        axis=1,
    )

    df["Recommendation"] = df.apply(
        lambda r: str(generate_recommendation(
            r["study_hours_per_day"],
            r["sleep_hours"],
            r["attendance_percentage"],
            r["assignment_completion"],
            r["test_score"],
        )),
        axis=1,
    )

    return df
