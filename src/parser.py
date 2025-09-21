import time

def read_lines_replay(path: str):
    """Read all lines in the log file once (replay mode)."""
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines_follow(path: str, poll_interval: float = 1.0):
    """
    Real-time mode: check the file every poll_interval seconds
    and yield new lines as they are added.
    """
    last_size = 0
    while True:
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                if len(lines) > last_size:
                    new_lines = lines[last_size:]
                    last_size = len(lines)
                    for line in new_lines:
                        yield line.rstrip('\n')
        except FileNotFoundError:
            pass  # If the file doesn't exist yet, just wait and retry
        time.sleep(poll_interval)
