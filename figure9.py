from datetime import datetime
import json

database = []

def process_logs(logs):
    severities = [log["severity"] for log in logs]
    sorted_severities = sorted(severities)
    high_severity = max(severities)
    high_index = sorted_severities.index(high_severity)
    return sorted_severities, high_index

def save_result(event_id, sorted_values, lookup_index):
    database.append({
        "event_id": event_id,
        "sorted": sorted_values,
        "lookup": lookup_index,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == "__main__":
    ui_logs = [
        {"timestamp": 16900001, "severity": 5},
        {"timestamp": 16900002, "severity": 2},
        {"timestamp": 16900003, "severity": 9}
    ]

    print("=== Web UI – Log Submission Panel ===")
    print("Entered Logs:")
    print(json.dumps(ui_logs, indent=2))

    sorted_vals, high_idx = process_logs(ui_logs)

    print("\nBackend Response:")
    print(f"Sorted Severity Values: {sorted_vals}")
    print(f"High Severity Index: {high_idx}")

    save_result("evt_003", sorted_vals, high_idx)

    print("\nPersistence Store (In-Memory):")
    print(json.dumps(database, indent=2))
