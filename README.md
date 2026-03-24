# SOC Password Security & Brute-Force Defense Lab

## Overview
Simulated a Security Operations Center workflow to detect brute-force attacks:

- Generates authentication logs with timestamps and IP addresses
- Simulates brute-force attacks on login system
- Detects suspicious login attempts using Python
- Sends alerts (console / Slack / email)
- Visualizes incidents in Splunk dashboards

## Features
- Threshold-based brute-force detection
- IP tracking and time-window analysis
- SIEM-ready log format
- SOC-style incident reporting

## How to Run
1. Simulate attacks: `python brute_force.py`
2. Detect attacks: `python detect_bruteforce.py`
