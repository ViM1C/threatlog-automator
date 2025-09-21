\# ThreatLog Automator



A Python-based log monitoring tool that detects failed logins and sudo usage from system logs.  

Supports \*\*real-time monitoring\*\* and \*\*replay mode\*\*, storing all alerts in a SQLite database.



---



\## Features

\- \*\*Replay Mode\*\*: Process existing log files for analysis  

\- \*\*Follow Mode\*\*: Real-time monitoring like `tail -f`  

\- \*\*IP + Username Extraction\*\*: Regex-based detection for each event  

\- \*\*SQLite Storage\*\*: All alerts saved for historical review  

\- \*\*Clean Output Viewer\*\*: Easy-to-read table of alerts  

\- \*\*Configurable\*\*: Log path and thresholds via `config.json`  



---



\## Installation

1\. Clone the repository:

&nbsp;  ```bash

&nbsp;  git clone https://github.com/YOUR-USERNAME/threatlog-automator.git

&nbsp;  cd threatlog-automator

&nbsp;  ```



2\. Create a virtual environment:

&nbsp;  ```bash

&nbsp;  python -m venv .venv

&nbsp;  . .venv/Scripts/activate   # Windows

&nbsp;  ```



3\. Install dependencies:

&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt

&nbsp;  ```



---



\## Usage

\### Replay Mode

Process existing log files:

```bash

python src/main.py --config config.json --mode replay

```



\### Follow Mode

Real-time monitoring for new log entries:

```bash

python src/main.py --config config.json --mode follow

```



---



\## View Alerts

Show all alerts stored in the database in a clean table:

```bash

python view\_alerts.py

```



---



\## Configuration

Edit `config.json` to change:

\- Log file path  

\- Detection thresholds  

\- Future email/Slack settings  



---



\## Sample Output

```

\[ALERT] failed\_login | time=2025-09-21T15:30:12 | ip=203.0.113.10 | user=admin | Sep 21 10:00:01 myhost sshd\[11111]: Failed password for invalid user admin

```



---



\## Next Steps

\- Add Slack or email alerts  

\- Build a simple web dashboard  

\- Support more log event types  



---



\## License

MIT License

