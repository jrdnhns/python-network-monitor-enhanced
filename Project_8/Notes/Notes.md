1. Import csv -Keep what you have and add:

from datetime import datetime
import subprocess
import time
import csv



2. Replace your targets list - Instead of only IPs, use a 
dictionary so your output is more descriptive:

devices = {
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1",
    "Default Gateway": "10.0.0.1"
}



3. Update your loop - Instead of:

for target in targets:

use

for name, target in devices.items():

Now every device has a readable name.



4. Add a timestamp - Before printing the status:

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



5. Improve the print statement - Instead of

print(f"{time.ctime()} - {target} is {status}")

print 

print(f"{timestamp} - {name} ({target}) - {status}")
