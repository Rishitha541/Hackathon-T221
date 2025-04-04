# simulate_requests.py
import requests
import time

URL = "http://127.0.0.1:5000"

for i in range(15):
    response = requests.get(URL)
    print(f"Request {i+1} - Status: {response.status_code}")
    time.sleep(3)  # send 1 request per second (adjust as needed)
