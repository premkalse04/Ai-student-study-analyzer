import sqlite3
import hashlib
from datetime import datetime

DB_PATH = "auth/users.db"

def get_db():
    return sqlite3.connect(DB_PATH)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_history_table():
    """Initialize the auth_history table if it doesn't exist"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS auth_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            action_type TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            ip_address TEXT,
            user_agent TEXT,
            status TEXT DEFAULT 'success'
        )
    """)
    conn.commit()
    conn.close()

def log_auth_event(email, action_type, status='success', ip_address=None, user_agent=None):
    """Log authentication events (login/signup) to history table"""
    init_history_table()
    conn = get_db()
    cur = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("""
        INSERT INTO auth_history (email, action_type, timestamp, ip_address, user_agent, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (email, action_type, timestamp, ip_address, user_agent, status))
    conn.commit()
    conn.close()

def get_auth_history(email=None, limit=100):
    """Retrieve authentication history. If email is provided, filter by email."""
    init_history_table()
    conn = get_db()
    cur = conn.cursor()
    if email:
        cur.execute("""
            SELECT * FROM auth_history 
            WHERE email = ? 
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (email, limit))
    else:
        cur.execute("""
            SELECT * FROM auth_history 
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (limit,))
    results = cur.fetchall()
    conn.close()
    return results

def create_user(email, password):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password TEXT,
            created_at TEXT
        )
    """)
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(
            "INSERT INTO users (email, password, created_at) VALUES (?, ?, ?)",
            (email, hash_password(password), timestamp)
        )
        conn.commit()
        # Log signup event
        log_auth_event(email, 'signup', status='success')
        return True
    except Exception as e:
        # Log failed signup attempt
        log_auth_event(email, 'signup', status='failed')
        return False
    finally:
        conn.close()

def authenticate_user(email, password):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, hash_password(password))
    )
    result = cur.fetchone()
    conn.close()
    
    # Log login attempt
    if result:
        log_auth_event(email, 'login', status='success')
        return True
    else:
        log_auth_event(email, 'login', status='failed')
        return False
