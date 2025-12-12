# Automated Battery Health Reminder System

A lightweight local Python-based system for monitoring stale smart-lock battery checks, sending reminders, and tracking CTR analytics.

## 📌 Project Overview

This project automates battery health reminders for smart locks.
It identifies locks that haven’t been checked in 30+ days, simulates sending reminder notifications, and tracks user engagement through click logs.

The system fulfills three primary goals:

✔ Identify inactive/stale locks
✔ Send automated reminders
✔ Measure user engagement (CTR analytics)

---

## 🎯 Objective

The main objective is to notify users automatically when their lock battery status has not been checked recently.
The system also tracks user clicks on notifications to measure effectiveness.

---

## 🧰 Tech Stack & Tools
Programming Language

- Python 3.x
- Libraries Used
- (All standard Python libraries — no external DB or cloud services)
- json → Mock database storage
- datetime → Stale lock calculation
- uuid → Campaign ID generation

---

## 📂 Local Mock Database Setup

- The system uses three JSON files acting as lightweight local databases:
- Purpose	File	Description
- Lock Data	locks.json	Simulates a DynamoDB lock-status table
- Notification Log	sent_notifications.json	Stores reminders sent
- Click Log	click_logs.json	Tracks user clicks on reminders
- These mock DBs make the system completely self-contained and runnable locally.

---

## 🏗 System Architecture
🔄 Flow Overview

1.Load Lock Data → Reads locks.json
2.Identify Stale Locks → Locks not checked in the last 30 days
3.Send Notification (Simulated)
4.Log Notification Activity → Writes to sent_notifications.json
5.Track User Clicks → CLI simulation
6.Generate CTR Summary → Using notification & click logs
7.This architecture allows complete offline execution and analysis.

---

## ▶️ How to Run the Project
1. Run the weekly reminder script
    python main.py
2. Simulate a notification click
    python -m analytics click <lock_id> <campaign_id>
3. Generate CTR summary
    python -m analytics summary <campaign_id>

---

## 📊 Findings

Based on sample logs and workflow 

Battery_Reminder_Project_Docume…
:
A. Users often forget battery checks
- Many locks crossed the 30-day threshold → users fail to monitor battery health.

B. Notifications improve engagement
CTR metrics show users respond when reminded.
Example:
- Notifications Sent: 10
- Clicks: 4
- CTR: 40%

C. CTR is a strong performance indicator
- High CTR → Good timing + helpful reminder
- Low CTR → Needs better wording/timing

D. Separate logs improve analytics
- sent_notifications.json + click_logs.json keep data clean and analyzable.

---

## 📈 Recommendations for Future Enhancements
☁️ 1. Migrate to Cloud (Production Version)

- AWS DynamoDB (lock data)
- AWS RDS PostgreSQL (user mapping)
- AWS Lambda (automated weekly runs)
- FCM (real push notifications)

## ✉️ 2. Improve Notification Content

- Estimated battery life
- Time since last check
- Strong CTA buttons

## 🎁 3. Introduce User Incentives

- Reward points or badges for regular maintenance.

## 📊 4. Add In-App Battery Dashboard

- Visualizations for
- Battery history
- Trends
- Predictions

## 🔮 5. Predict Battery Failure

Simple ML logic to predict potential battery drain.

---

## 📎 Repository Structure (Suggested)
/
│── main.py
│── analytics/
│     ├── __init__.py
│     ├── click.py
│     ├── summary.py
│── locks.json
│── sent_notifications.json
│── click_logs.json
│── README.md

---

##🌐 GitHub Repository

https://github.com/Bharath-B1805/Atomberg_Battery_Remainder
