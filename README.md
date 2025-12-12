🔋 Battery Health Reminder System (Python Local Version)
---
A Python-based automated reminder system that detects stale smart lock battery updates, sends simulated notifications, and tracks user engagement (click tracking).
Designed to run locally, without AWS, using simple JSON files as mock databases.

📌 Features
✅ Detect stale locks
Reads mock lock data from locks.json
Identifies locks not checked in the last 30 days

✅ Send simulated notifications
Generates a unique campaign ID for each weekly run
Logs all notifications in sent_notifications.json

✅ Track user click interactions
CLI-based “click” simulation
Stores clicks in click_logs.json

✅ Campaign analytics
Computes:
Notifications Sent
Clicks
CTR (Click-Through Rate)

Displays a professional campaign summary

📁 Project Structure
battery-reminder-project/
│
├── src/
│   ├── main.py
│   ├── dynamo.py
│   ├── analytics.py
│   └── __init__.py
│
├── data/
│   ├── locks.json
│   ├── sent_notifications.json
│   └── click_logs.json
│
├── config/
│   └── (optional future configs)
│
└── venv/ (Python virtual environment)

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/battery-reminder-project.git
cd battery-reminder-project

2. Create & activate virtual environment
Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

Linux / macOS:
python3 -m venv venv
source venv/bin/activate

3. Add sample lock data

Update/Create data/locks.json:

[
  { "lock_id": "L001", "last_checked": "2024-10-01T00:00:00" },
  { "lock_id": "L002", "last_checked": "2025-01-01T00:00:00" },
  { "lock_id": "L003", "last_checked": "2024-05-15T10:30:00" }
]

🚀 How to Run the System
Run the weekly reminder job
python src/main.py


Sample Output:

Starting weekly battery reminder job...
Campaign ID: 123e4567-e89b-12d3-a456-426614174000Found 2 stale locks.
Sending FCM notification to lock L001
Logged SENT notification for L001
Sending FCM notification to lock L003
Logged SENT notification for L003
Job complete.

🖱 Simulate User Click Tracking
1. Log a click
python -m src.analytics click L001 <campaign_id>


Adds a record to click_logs.json.

2. View campaign summary
python -m src.analytics summary <campaign_id>


Example Output:

Campaign Summary
-------------------------
Campaign ID: 123e4567-e89b-12d3-a456-426614174000
Notifications Sent: 2
Clicks: 1
CTR: 50.0%

📊 How CTR (Click Through Rate) Works
CTR = (Total Clicks / Total Notifications Sent) × 100
Used to measure:
User engagement
Effectiveness of reminders
Interest in battery maintenance

🧱 Future Enhancements
This local simulation can be expanded into a full production system:

🔹 Migration to AWS (optional)
DynamoDB → lock data
PostgreSQL (RDS) → user-lock mapping
AWS Lambda → weekly automation
FCM → real notifications

🔹 UI Dashboard for reports
Charts for CTR
Lock status overview

🔹 Predictive alerts
Estimate battery life
Predict failure before it happens

📄 Project Report
A full 2-page project submission is included in the documentation section of this repository.

🤝 Contributions
Pull requests and feature suggestions are welcome!
This project is intentionally simple and educational — perfect for beginners learning automation logic.

📜 License
This project is released under the MIT License.

👨‍💻 Author
Bharath B AI Internship Assignment — Atomberg
