import json
import pytz
from datetime import datetime

class counts:
  def __init__(self):
    with open("counts.json","r") as f:
      _=json.load(f)
    
  def add(self,n):
    with open("counts.json","r") as f:
      f=json.load(f)
      
    _=datetime.now(tz=pytz.timezone("Asia/Kolkata"))
    _1=" am"
    _2=int(_.hour)
    if _2 > 12:
      _1=" pm"
      _2 -= 12
    _2=str(_2)
    _3=str(_.minute)
    f[n]=f"{_2}:{_3}{_1}"
    print(f"{n} server is online\nLast Checked {f[n]}")
    
    with open("counts.json","w") as f1:
      json.dump(f,f1, indent=2)