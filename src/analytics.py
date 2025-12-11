import json
from datetime import datetime

SENT_LOG = "../data/sent_notifications.json"
CLICK_LOG = "../data/click_logs.json"

def log_sent_notification(lock_id, campaign_id):
    entry = {"lock_id": lock_id, "campaign_id": campaign_id, "timestamp": datetime.utcnow().isoformat()}
    _append_json(SENT_LOG, entry)
    print(f"Logged SENT notification for {lock_id}")

def log_click(lock_id, campaign_id):
    entry = {"lock_id": lock_id, "campaign_id": campaign_id, "timestamp": datetime.utcnow().isoformat()}
    _append_json(CLICK_LOG, entry)
    print(f"Logged CLICK for {lock_id}")

def _append_json(path, obj):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except:
        data = []
    data.append(obj)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def campaign_summary(campaign_id):
    sent = _load_all(SENT_LOG)
    clicks = _load_all(CLICK_LOG)
    sent_count = sum(1 for e in sent if e["campaign_id"] == campaign_id)
    click_count = sum(1 for e in clicks if e["campaign_id"] == campaign_id)
    ctr = round((click_count / sent_count) * 100, 2) if sent_count > 0 else 0
    print(f"\nCampaign {campaign_id} Summary: Sent={sent_count}, Clicks={click_count}, CTR={ctr}%")

def _load_all(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m src.analytics click <lock_id> <campaign_id> OR summary <campaign_id>")
        sys.exit()
    cmd = sys.argv[1]
    if cmd == "click":
        log_click(sys.argv[2], sys.argv[3])
    elif cmd == "summary":
        campaign_summary(sys.argv[2])