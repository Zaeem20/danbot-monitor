# Auto Setup Script
import json
import time
import platform
import os


#this is auto setup script which make json file 
print("\033[1;92m")

print("Auto Setup Script")
print('')
time.sleep(2)
apikey = input("Enter API key:- ")
bsid = input("Enter BSID:- ")
psid = input("Enter PSID:- ")
psnode = int(input("Enter PSNode no:- "))
bsnode = int(input("Enter BSNode no:- "))
data={}
data["apikey"]=apikey
data["bsid"]=bsid
data["psid"]=psid
data["psnode"]=psnode
data["bsnode"]=bsnonde
try:
  with open("config.json", "w") as a:
    json.dump(data,a, indent=2)
    print(" ")
    print("Operation Completed")
    print("Executing main file")
    time.sleep(3)
    if platform.system() == 'Linux':
      os.system("clear")
      os.system("python null.py")
    elif platform.system() == 'Windows':
      os.system("cls")
      os.system("python main.py")
except:
  print("Operation Failed")
