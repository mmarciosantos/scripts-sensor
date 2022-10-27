import requests

url = f"https://demo.thingsboard.io/api/v1/{ACCESS_TOKEN}/telemetry"

payload = {
    "temperature": 25,
    "humidity": 50
}

headers = {
    "Authorization": f"Bearer {JWT_TOKEN}",
    "content-type": "application/json",
}

response = requests.post(url=url, json=payload, headers=headers)
