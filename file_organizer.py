import os
import shutil
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folders=["Images","Documnets","Python","Music","Executables","C Prg"]
for folder in folders:
    os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)
try:
    for file in os.listdir():
        if os.path.isfile(file):  # only files, not folders
            print(file)

        if file.endswith(".jpg") or file.endswith(".png"):
            shutil.move(file,"Images/" + file)
        elif file.endswith(".pdf"):
            shutil.move(file,"Documents/" + file)
        elif file.endswith(".py"):
            shutil.move(file,"Python/" + file)
        elif file.endswith(".mp3") :
            shutil.move(file,"Music/" + file)
        elif file.endswith(".exe"):
            shutil.move(file,"executables/"+file)
        elif file.endswith(".c"):
            shutil.move(file,"C prg/" +file)

except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("Permission Denied")
except Exception as e:
    print(e)
print("Organization completed successfullly")