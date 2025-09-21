import sqlite3

DB_PATH = "alerts.db"

def view_alerts():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    rows = c.execute("SELECT ts, etype, ip, user, msg FROM alerts")

    print("Timestamp                  | Event Type    | IP              | User       | Message")
    print("-" * 100)

    for ts, etype, ip, user, msg in rows:
        ip_display = ip if ip else "-"
        user_display = user if user else "-"
        print(f"{ts:25} | {etype:<12} | {ip_display:<15} | {user_display:<10} | {msg}")

    conn.close()

if __name__ == "__main__":
    view_alerts()
