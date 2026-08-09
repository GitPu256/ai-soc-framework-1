import json

def process_logs(logs):
    severities = [log["severity"] for log in logs]
    sorted_severities = sorted(severities)
    high_severity = max(severities)
    high_index = sorted_severities.index(high_severity)
    return {
        "sorted": sorted_severities,
        "high_severity_index": high_index,
        "status": "Processed successfully"
    }

if __name__ == "__main__":
    request_body = {
        "logs": [
            {"timestamp": "16900001", "severity": 5, "event": "A"},
            {"timestamp": "16900002", "severity": 2, "event": "B"},
            {"timestamp": "16900003", "severity": 9, "event": "C"}
        ]
    }

    print("=== Swagger UI – /process_logs (POST) ===")
    print("Request Body (JSON):")
    print(json.dumps(request_body, indent=2))

    response = process_logs(request_body["logs"])

    print("\nResponse (200 OK):")
    print(json.dumps(response, indent=2))

