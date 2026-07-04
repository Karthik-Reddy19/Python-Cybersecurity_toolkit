import string
import random
import os
import shutil
from pathlib import Path
import time 
import requests
from datetime import datetime
from socket import *
import socket
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def password_genarator(n):
    letters=string.ascii_letters
    numbers=string.digits
    symbols=string.punctuation
    all_characters=letters+numbers+symbols
    password=""
    for i in range (n):
        password+=random.choice(all_characters)
    return password
# a=int(input("ENter the password length"))
# print(password_genarator(a))
def file_organizer():
    folders=["Documents","Music","Python","Image"]
    for folder in folders :
        os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)
    try:
        for file in os.listdir(BASE_DIR):

            source = os.path.join(BASE_DIR, file)

            if not os.path.isfile(source):
                continue

            if file.endswith((".jpg", ".png")):
                shutil.move(source, os.path.join(BASE_DIR, "Image", file))

            elif file.endswith(".pdf"):
                shutil.move(source, os.path.join(BASE_DIR, "Documents", file))

            elif file.endswith(".mp3"):
                shutil.move(source, os.path.join(BASE_DIR, "Music", file))

            elif file.endswith(".py"):
                shutil.move(source, os.path.join(BASE_DIR, "Python", file))
        
    except PermissionError:
        print("Permission Denied")
    except FileNotFoundError:
        print("File not found ")
    except Exception as e:
        print(e)    
# n=file_organizer()
# print(n)
def website_monitor():
    try:
        n=input("Enter the name of the website")
        start=time.time()
        response=requests.get(n, timeout=5)
        sc=response.status_code
        print(sc)
        end=time.time()
        rt=round((end-start),2)
        if sc==200:
            print("Website is Online")
        else:
            print("Website is Down")
        with open("log.txt","a") as file:
            file.write("\n----Log Report-----\n")
            file.write(f"{datetime.now()}\n")
            file.write(f"Status code: {sc}\n")
            file.write(f"Response time:{rt}")
            file.write("-"*40 +"\n")
    except requests.exceptions.ConnectionError:
        print("Connection Failed")
    except requests.exceptions.Timeout:
        print("TImeout Error")
# s=website_monitor()
# print(s)
def port_scanner():
    host=input("Enter the name of the host")
    port=int(input("Enter the port number"))
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=sock.connect_ex((host,port))
    sock.close()
    if result==0:
        print("[open]",port)
    else:
        print("[close]",port)
# s=port_scanner()
# print(s)
def log_analyzer():
    log_file = os.path.join(BASE_DIR, "sample.log")

    with open(log_file, "r") as file:
        lines=file.readlines()
        for line in lines:
           print(line.strip())
        error=0
        for line in lines:
            if "ERROR" in line:
                error+=1
        print("Error:",error)
        info=0
        for line in lines:
            if "INFO" in line:
                info+=1
        print("Info:",info)
        warning=0
        for line in lines:
            if "WARNING" in line:
                warning+=1
        print("Warning:",warning)

# l=log_analyzer()
# print(l)
while True:
    print("""
    ========== Cyber Security Toolkit ==========
    1. Password Generator
    2. File Organizer
    3. Website Monitor
    4. Port Scanner
    5. Log Analyzer
    6. Exit
    ============================================
    """)
    choice=int(input("ENter the choice number:"))

    if choice==1:
        p=int(input("ENter the password length"))
        print(password_genarator(p))
    elif choice==2:
        f=file_organizer()
        print(f)
    elif choice==3:
        w=website_monitor()
        print(w)
    elif choice==4:
        p=port_scanner()
        print(p)
    elif choice==5:
        l=log_analyzer()
        print(l)
    elif choice==6:
        print("Exitting-----")
        break
    else:
        print("Enter the correct option (1-6)")






