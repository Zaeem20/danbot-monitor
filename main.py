from datetime import datetime
from danbotstatus import dbhs
from webserver import keep_alive,_uptime,run
from schedule import every, repeat, run_pending, run_all
import requests
from counts import counts
import time
import os
import json
Count=counts()

with open("config.json", "r") as f:
  o=json.load(f)

api = o["apikey"]
psid = o["psid"]
bsid = o["bsid"]

def rcheck(server):
  url=f'https://panel.danbot.host/api/client/servers/{server}/resources'

  headers = {
      "Authorization": f"Bearer {api}",
      "Accept": "application/json",
      "Content-Type": "application/json",
  }

  response = requests.request('GET', url, headers=headers)
  o = response.text.split("{")[2].split(",")[0].split(":")[1].split('"')[1]

  return o


def ps(choice):
    url = f'https://panel.danbot.host/api/client/servers/{psid}/power'
    headers = {
        "Authorization": f"Bearer {api}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    payload = {"signal": choice}

    response = requests.request('POST', url,json=payload, headers=headers)
    p="p"
    o = rcheck(psid)
    if 'running' or 'starting' or 'stopping' not in o:
      print(f"Primary server is {choice+p if choice=='stop' else choice}ing Now {response.text}")
    else:
      return

def bs(choice):
    url = f'https://panel.danbot.host/api/client/servers/{bsid}/power'
    headers = {
        "Authorization": f"Bearer {api}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    payload = {"signal": choice}

    response = requests.request('POST', url,json=payload, headers=headers)
    p="p"
    o = rcheck(bsid)
    if "running" or 'starting' or 'stopping' not in o:
      print(f"Backup server is {choice+p if choice=='stop' else choice}ing Now {response.text} ")
    else:
      return
    

@repeat(every(5).minutes)
def n16():
    o = dbhs.getnodestatus(16)
    return o['is_vm_online']
    


@repeat(every(5).minutes)
def n10():
    o = dbhs.getnodestatus(10)
    return o['is_vm_online']

def _1():
  node10,node16=n10(),n16()
  if not node10 and not node16:
    print("Both servers are down")
  elif node10 and node16:
    print("Both server are running\nUsing Primary Server")
    ps("kill")
    Count.add("both")
    bs("start")
  elif node16:
    print("Outage in node10\nStill using primary server")
    Count.add("node16")
    ps("start")
  elif node10:
    print("Outage in node16\nmoving to node10\nBackup Server")
    Count.add("node10")
    bs("start")
    

import asyncio
run=asyncio.get_event_loop().run_until_complete

keep_alive()
while True:
  _1()
  run(_uptime())
  time.sleep(5*60)


