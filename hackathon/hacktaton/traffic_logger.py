from datetime import datetime
import os

LOG_FILE = 'traffic_log.txt'
BLOCKED_IPS_FILE = 'blocked_ips.txt'

def log_request(ip):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{ip},{datetime.now()}\n")

def is_ip_blocked(ip):
    if not os.path.exists(BLOCKED_IPS_FILE):
        return False
    with open(BLOCKED_IPS_FILE, 'r') as f:
        return ip in f.read()
