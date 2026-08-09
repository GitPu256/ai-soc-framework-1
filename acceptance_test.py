import requests

payload = {
    "severities": [3, 8, 2, 5, 9, 1, 7],
    "lookup_value": 8
}

response = requests.post("http://127.0.0.1:8000/logs/process", json=payload)

print("ACCEPTANCE TEST START")
print("Input:", payload)
print("API Response:", response.json())
print("Status Code:", response.status_code)
print("ACCEPTANCE TEST COMPLETE")
