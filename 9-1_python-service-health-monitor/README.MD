Project 9.1 – Python Service Health Monitor: Persistent Logging

Overview
Project 9.1 expands the Python network monitoring tool developed in Project 8 by introducing persistent logging. Instead of displaying monitoring results only in the terminal or Jenkins console, the application now records timestamped health checks to a dedicated log file.
This enhancement moves the project closer to a NOC-style monitoring workflow by creating a historical record of device availability that can be reviewed after execution.

Objectives
• Maintain continuous network reachability checks.
• Preserve console output for real-time monitoring.
• Record each monitoring result to a persistent log file.
• Prepare the application for future alerting and service health checks.

Features
• Continuous monitoring loop
• Named network devices
• Timestamped status reporting
• ICMP reachability testing using Python subprocess
• Console output
• Persistent logging to monitoring.log

Technologies Used
• Python 3
• Linux (Ubuntu)
• Jenkins
• Git
• GitHub
• AWS EC2

How It Works
The monitoring tool continuously checks configured network targets using the system ping command.
For each device the script:
1. Sends an ICMP echo request.
2. Determines whether the device is UP or DOWN.
3. Generates a timestamp.
4. Displays the result in the console.
5. Appends the same result to monitoring.log.
Example output:
2026-06-27 14:30:01 - Google DNS (8.8.8.8) - UP
2026-06-27 14:30:02 - Cloudflare DNS (1.1.1.1) - UP
2026-06-27 14:30:03 - Default Gateway (10.0.0.1) - UP

Repository Structure
python-service-health-monitor/
├── service_health_monitor.py
├── monitoring.log
├── README.md
├── commands/
├── notes/
└── screenshots/

Skills Demonstrated
• Python automation
• Network monitoring fundamentals
• File I/O and persistent logging
• Linux command-line execution
• Jenkins job automation
• Git version control
• GitHub project management

Future Enhancements (Project 9)
• Alert generation for failed health checks
• Service health monitoring
• HTTP response validation
• SSH availability checks
• Log rotation
• Email or webhook notifications
• Expanded device inventory

Project Outcome
Project 9.1 establishes the logging foundation for the monitoring application by preserving health check results beyond the console session. This provides historical visibility into device availability and prepares the application for alerting and additional service monitoring capabilities in future milestones.

