import requests
import time
from datetime import datetime
try:
    website = input("Enter the name of the website:")
    start=time.time()
    response=requests.get(website)
    sc=response.status_code
    print(sc)
    end=time.time()
    rt=round(end-start,3)
    print("Response Time:",rt,"seconds")
    if sc==200:
        print("Website is ONLINE")
    else:
        print("Website may be DOWN")
    with open ("uptime_log.txt","a") as file:
        file.write(f"{datetime.now()}\n")
        file.write("Uptime Log\n")
        file.write(f"Response Time:{rt} seconds\n")
        file.write(f"Status code:{sc} \n")

except requests.exceptions.ConnectionError:
    print("Connection Failed")
except requests.exceptions.ConnectTimeout:
    print("Connection Timed out")
except Exception as e:
    print(e)
