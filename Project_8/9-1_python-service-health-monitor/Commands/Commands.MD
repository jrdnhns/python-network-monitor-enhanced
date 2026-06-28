service_health_monitor.py
LOG_FILE = "monitoring.log"
message = f"{timestamp} - {name} ({target}) - {status}"
print(message)
with open(LOG_FILE, "a") as log:
    log.write(message + "\n")