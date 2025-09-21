import sqlite3

DB_PATH = "alerts.db"

def init_db():
    """Create alerts table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            ts TEXT,
            etype TEXT,
            ip TEXT,
            user TEXT,
            msg TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_alert(ts, etype, ip, user, msg):
    """Save a single alert to the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO alerts (ts, etype, ip, user, msg) VALUES (?, ?, ?, ?, ?)",
                 (ts, etype, ip, user, msg))
    conn.commit()
    conn.close()
