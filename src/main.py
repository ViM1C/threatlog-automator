import json
import argparse
from parser import read_lines_replay, read_lines_follow
from detector import process_line
from storage import init_db, save_alert

def load_config(path):
    with open(path) as f:
        return json.load(f)

def main():
    # Command-line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='config.json')
    ap.add_argument('--mode', choices=['replay', 'follow'], default='replay')
    args = ap.parse_args()

    # Load config and init database
    cfg = load_config(args.config)
    init_db()

    # Choose replay or follow mode
    reader = read_lines_follow if args.mode == 'follow' else read_lines_replay

    # Process each log line
    for line in reader(cfg["log_path"]):
        event = process_line(line)
        if event:
            etype, ts, ip, user, msg = event
            print(f"[ALERT] {etype} | time={ts} | ip={ip} | user={user} | {msg}")
            save_alert(ts, etype, ip, user, msg)

if __name__ == "__main__":
    main()
