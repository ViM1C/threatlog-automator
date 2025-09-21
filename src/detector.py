import re
from datetime import datetime

# Regex patterns for IP and username
IP_REGEX = re.compile(r'\b\d{1,3}(?:\.\d{1,3}){3}\b')
USER_REGEX = re.compile(r'for invalid user (\w+)')

def process_line(line: str):
    """
    Process a single log line.
    Detect failed logins or sudo usage.
    Extract IP and username if available.
    """
    text = line.lstrip('\ufeff')  # remove BOM if present
    ts_iso = datetime.utcnow().isoformat()

    ip_match = IP_REGEX.search(line)
    user_match = USER_REGEX.search(line)

    ip_addr = ip_match.group(0) if ip_match else None
    username = user_match.group(1) if user_match else None

    if "Failed password" in text:
        return ("failed_login", ts_iso, ip_addr, username, line.strip())

    if "sudo" in text:
        return ("sudo_usage", ts_iso, ip_addr, username, line.strip())

    return None
