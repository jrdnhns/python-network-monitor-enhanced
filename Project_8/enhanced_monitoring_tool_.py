from datetime import datetime
import subprocess
import time
import csv

targets = ["8.8.8.8", "10.0.0.1", "10.0.0.238"]
devices = {
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1",
    "Default Gateway": "10.0.0.1"
}


while True:
    print("\n-- Network Check --")

    for name, target in devices.items():
        result = subprocess.run(
            ["ping", "-c", "2", target],
            stdout=subprocess.DEVNULL
        )
    
        status = "UP" if result.returncode == 0 else "DOWN"
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - {name} ({target}) - {status}")

    time.sleep(10)
