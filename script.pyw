import time
from datetime import datetime as dt
#Creating a variable to access the Host file
host_path = "C:\Windows\System32\drivers\etc\hosts"
#Redirect_path
redirect_path = "127.0.0.1"
#List of website name you want to block
website_list = ["www.facebook.com","facebook.com"]

#Checking Timing

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,7) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,13):
        print("Working Hours...")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect_path+ " " +website+"\n")
    else:
        print("Fun Hours...")
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        time.sleep(4)
