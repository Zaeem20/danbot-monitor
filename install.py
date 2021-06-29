# Auto Setup Script
import json
import time
import os


#this is auto setup script which make json file 
print("033\[1;92m")

print("Auto Setup Script")
print 
time.sleep(2)
apikey = input("Enter API key:- ")
bsid = input("Enter BSID")
psid = input("Enter PSID")
data={}
data["apikey"]=apikey
data["bsid"]=bsid
data["psid"]=psid
try:
  with open("config.json", "w") as a:
    json.dump(data,a, indent=2)
except:
  print("Operation Failed")
