import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
hosts_temp="hosts"
redirect = "127.0.0.1"

website_list=["www.facebook.com","facebook.com","netflix"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,15,48) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,15,50):
        # print("working")
        with open(hosts_path,'r+') as file:
            content=file.read()
            # print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        # print("play")
         with open(hosts_path,'r+') as file:
            content=file.readlines()
            # print(content)
            file.seek(0) #keeps pointer at first character
            for line in content:
                if not any( website in line for website in website_list):
                    file.write(line)
            file.truncate()


    time.sleep(10)