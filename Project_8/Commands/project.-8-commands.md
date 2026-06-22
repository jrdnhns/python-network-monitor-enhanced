import csv

devices = {
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1",
    "Default Gateway": "10.0.0.1"
}

for name, target in devices.items():

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"{timestamp} - {name} ({target}) - {status}")




