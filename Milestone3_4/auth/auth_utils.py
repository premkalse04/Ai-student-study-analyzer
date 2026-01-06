import sqlite3
import hashlib
from datetime import datetime
from pathlib import Path

# =========================================================
# DB PATH (SAFE & RELATIVE)
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "users.db"


# =========================================================
# DB HELPERS
# =========================================================
def get_db():
    return sqlite3.connect(DB_PATH)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# =========================================================
# AUTH HISTORY
# =========================================================
def init_history_table():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS auth_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            action_type TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            status TEXT DEFAULT 'success'
        )
    """)
    conn.commit()
    conn.close()


def log_auth_event(email, action_type, status="success"):
    init_history_table()
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO auth_history (email, action_type, timestamp, status)
        VALUES (?, ?, ?, ?)
        """,
        (
            email,
            action_type,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status,
        ),
    )
    conn.commit()
    conn.close()


# =========================================================
# USER MANAGEMENT
# =========================================================
def init_user_table():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def user_exists(email: str) -> bool:
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM users WHERE email = ?", (email,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists


def create_user(email: str, password: str) -> bool:
    init_user_table()

    email = email.strip().lower()

    if user_exists(email):
        log_auth_event(email, "signup", status="failed")
        return False

    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO users (email, password, created_at)
            VALUES (?, ?, ?)
            """,
            (
                email,
                hash_password(password),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ),
        )
        conn.commit()
        conn.close()

        log_auth_event(email, "signup", status="success")
        return True

    except sqlite3.IntegrityError:
        log_auth_event(email, "signup", status="failed")
        return False


def authenticate_user(email: str, password: str) -> bool:
    email = email.strip().lower()
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT 1 FROM users WHERE email = ? AND password = ?",
        (email, hash_password(password)),
    )
    user = cur.fetchone()
    conn.close()

    if user:
        log_auth_event(email, "login", status="success")
        return True
    else:
        log_auth_event(email, "login", status="failed")
        return False


# =========================================================
# ADMIN HELPERS (FIXED – NOT NESTED)
# =========================================================
def get_all_users():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT email, created_at
        FROM users
        ORDER BY created_at DESC
    """)
    users = cur.fetchall()
    conn.close()
    return users


def get_all_auth_history(limit=200):
    init_history_table()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT email, action_type, timestamp, status
        FROM auth_history
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    history = cur.fetchall()
    conn.close()
    return history
