import requests
import random

url = "http://127.0.0.1:8000/apply"
names = ["Thabo", "Sarah", "Kofi", "Zanele", "Lwazi"]

print("🚀 Starting Stress Test: Sending 100 applications...")

for i in range(100):
    payload = {
        "name": random.choice(names),
        "score": random.randint(300, 850),
        "income": random.randint(10000, 60000),
        "expenses": random.randint(5000, 20000)
    }
    # We send the data as 'params' because our API uses URL parameters
    response = requests.post(url, params=payload)
    print(f"Request {i+1}: {response.status_code}")

print("✅ Stress Test Complete. Check your database!")