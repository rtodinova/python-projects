# This is a Website Blocker for Windows users.
import time
from datetime import datetime

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"

redirect_url="127.0.0.1"
websites_to_block=["www.facebook.com", "facebook.com"]

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

while True:
    if datetime(year, month, day, 8) < datetime.now() < datetime(year, month, day, 16):
        with open(hosts_path, 'r+') as hosts_file:
            content = hosts_file.read()
            for website in websites_to_block:
                if website in content:
                    pass
                else:
                    line = redirect_url + " " website + "\n"
                    hosts_file.write(line)
    else:
        with open(hosts_path, 'r+') as hosts_file:
            content = hosts_file.readlines() #content is a list
            hosts_file.seek(0)
            for line in content:
                if not any(website in line for website in websites_to_block):
                    hosts_file.write(line)
            hosts_file.truncate()
    time.sleep(5)
