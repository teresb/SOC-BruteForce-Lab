from collections import defaultdict

LOG_FILE = "auth.log"
THRESHOLD = 3

failures = defaultdict(int)
ip_tracker = defaultdict(list)

with open(LOG_FILE, "r") as f:
    for line in f:
        parts = line.strip().split(" - ")
        username = parts[1]
        status = parts[2]
        ip = parts[3]

        if status == "FAILED":
            failures[username] += 1
            ip_tracker[username].append(ip)

for user, count in failures.items():
    if count >= THRESHOLD:
        print(f"[ALERT] Brute-force attack on {user}")
        print(f"Failed attempts: {count}")
        print(f"Attacker IPs: {ip_tracker[user]}")