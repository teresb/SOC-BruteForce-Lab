import time
import random

users = {
    "admin": "password123"
}

LOG_FILE = "auth.log"

def generate_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

def log_event(username, status, ip):
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.ctime()} - {username} - {status} - {ip}\n")

def login(username, password):
    ip = generate_ip()
    if username in users and users[username] == password:
        log_event(username, "SUCCESS", ip)
        return True
    else:
        log_event(username, "FAILED", ip)
        return False