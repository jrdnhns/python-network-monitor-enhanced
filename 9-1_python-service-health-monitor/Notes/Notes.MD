First step for Project 9.1:

1. Make a copy of your working Project 8 script and 

2. rename it:
service_health_monitor.py
I didn't edit the working Project 8 file directly.
Your folder should become:
python-service-health-monitor/
├── service_health_monitor.py
├── README.md
├── screenshots/
├── commands/
└── notes/

3. Then your first code change is only adding a log file name near the top:
LOG_FILE = "monitoring.log"

That’s it for the first move.
Project 9.1 goal is simple:
Take the working timestamped monitor and begin preparing it to write results into monitoring.log 
instead of only printing to Jenkins Console Output.

4. Create the message once
Right after:
status = "UP" if result.returncode == 0 else "DOWN"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
replace:
print(f"{timestamp} - {name} ({target}) - {status}")
with:
message = f"{timestamp} - {name} ({target}) - {status}"
print(message)
This creates the output once so it can be reused.

5. Write the same message to the log
Immediately below:
print(message)
add:
with open(LOG_FILE, "a") as log:
    log.write(message + "\n")

Your finished section should look like this:
status = "UP" if result.returncode == 0 else "DOWN"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"{timestamp} - {name} ({target}) - {status}"
print(message)
with open(LOG_FILE, "a") as log:
    log.write(message + "\n")

Goal:
Modifying the existing monitoring tool, push the changes to GitHub, and validate the update 
through an automated Jenkins build running on an AWS-hosted Linux server.

