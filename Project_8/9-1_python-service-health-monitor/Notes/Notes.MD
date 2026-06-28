First step for Project 9.1:

1. Make a copy of your working Project 8 script 
	
2. rename it:
service_health_monitor.py

3. Then your first code change is only adding a log file name near the top:
LOG_FILE = "monitoring.log"

4. & 5 Create the message once
Right after:
status = "UP" if result.returncode == 0 else "DOWN"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
replace:
print(f"{timestamp} - {name} ({target}) - {status}")
with:
message = f"{timestamp} - {name} ({target}) - {status}"
print(message)
This creates the output once so it can be reused.

6. Write the same message to the log
Immediately below:
print(message)
add:
with open(LOG_FILE, "a") as log:
    log.write(message + "\n")

7. Copy Jenkins EC2 Public IP after EC2 instance start.
	
8. SSH from PowerShell to AWS Ec2 Jenkins-Controller.
	
9. Launch Jenkins Dashboard > http://18.216.225.71:8080

10. Click New-Item.
  
11. In Jenkins, duplicate or create a new job named:
python-service-health-monitor-logging

12. Description of the Build.

13. In Source Code Management, point it to your existing repo:
https://github.com/jrdnhns/python-network-monitor-enhanced

14. In Build Steps → Execute shell, use the path where you uploaded it. If you upload it under Project_9, use:
cd Project_9/9.1-python-service-health-monitor
timeout 30s python3 -u service_health_monitor.py || true
ls -la
cat monitoring.log

15. Click Build Now.

16. Open Console Output.

17. Repository path error.
	
18. Confirmed Jenkins retrieval path from the latest project files directly from the GitHub repository, ensuring each build 
runs against the most recent version of the monitoring application.
	
19. Updated the execution path to match the renamed project directory, allowing Jenkins to locate the monitoring script 
and successfully automate the build process. 

20. Another Build Failure.

21. Discovered Line 22 TabError issue.
	
22. Spotted Line 22 TabError issue.
	
23. Corrected Line 22 by aligning with 21.
	
24. Build Now.
	
25. Still an issue with Line 22.
	
26. Instead of using 2 tabs, 8 spaces were used for Line 22..
	
27. Build Now.
	
28. Another Build Failure. Investigating, Console Output.
	
29. Now the issues with Line 24, another line IndentationError.. This time, 
4 spaces in from current position.
	
30. Fixed Line 24 and 25.
	
31. Build #9 Build Now.
	
32. Successfully completed Build 9, confirming the Jenkins pipeline retrieved the latest 
GitHub code, executed the enhanced monitoring script, generated the monitoring log, and completed 
the CI/CD workflow without errors.


Goal:
Modifying the existing monitoring tool, push the changes to GitHub, and validate the update 
through an automated Jenkins build running on an AWS-hosted Linux server.

