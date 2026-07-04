import os
with open(r"C:\Users\Public\automation\week3-project\sample.log","r") as file:
    lines=file.readlines()
for line in lines:
    print(line.strip())
error_count=0
for line in lines:
    if "ERROR" in line:
        error_count+=1
print("Errors:",error_count)
warning_count=0
for line in lines:
    if "WARNING" in line:
        warning_count+=1
print("Warnings:",warning_count)
info_count=0
for line in lines:
    if "INFO" in line:
        info_count+=1
print(info_count)
print("-------Error Logs-----")
for line in lines:
    if "ERROR" in line:
        print(line.strip())
keyword=input("Enter the keyword:").upper()
for line in lines:
    if keyword in line.upper():
        print(line.strip())
with open("report.txt","w") as report:
    report.write("---Log Analysis Report---\n")
    report.write(f"Errors:{error_count}\n")
    report.write(f"Warnings:{warning_count}\n")
    report.write(f"Info:{info_count}\n")