import time
from datetime import datetime as dt
x=0
f_path = "D:\Learning\Python\path\host.txt"
red="127.0.0.1"
website_list = ["www.facebook.com", "www.google.com"]
while x < 5:
    if dt(dt.now().year, dt.now().month,dt.now().day,10)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,11):
        with open(f_path, 'r+') as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write("\n" + red + " " + website)
        print("Work")

    else:
        with open(f_path, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
            f.truncate()
        print("fun")
    time.sleep(5)
    x=x+1
