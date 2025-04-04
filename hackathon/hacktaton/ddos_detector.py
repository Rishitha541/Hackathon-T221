from collections import defaultdict
from datetime import datetime, timedelta
import time

LOG_FILE = 'traffic_log.txt'
BLOCKED_IPS_FILE = 'blocked_ips.txt'
THRESHOLD =1  # requests per minute

def detect_ddos():
    ip_requests = defaultdict(list)
    now = datetime.now()

    with open(LOG_FILE, 'r') as f:
        for line in f:
            ip, timestamp = line.strip().split(',')
            timestamp = datetime.fromisoformat(timestamp)
            if now - timestamp < timedelta(minutes=1):
                ip_requests[ip].append(timestamp)

    for ip, times in ip_requests.items():
        if len(times) > THRESHOLD:
            block_ip(ip)

def block_ip(ip):
    with open(BLOCKED_IPS_FILE, 'a') as f:
        f.write(f"{ip}\n")
    print(f"[!] IP {ip} blocked for suspicious activity.")

if __name__ == '__main__':
    while True:
        detect_ddos()
        time.sleep(30)  # Check every 30 seconds
