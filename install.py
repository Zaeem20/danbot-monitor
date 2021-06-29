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

try:
  with open("config.json", "w") as a:
    json.dumps("apikey" , apikey)
    json.dumps("bsid" , bsid)
    json.dumps("psid" , psid)
except:
  print("Operation Failed")
"""
