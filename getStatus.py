import requests
import threading
import time


print(
'''
=========================================================
|                                                       |
|                                                       |
|         ██▓▒­░⡷⠂  GetStatus by Vivek ⠐⢾░▒▓██          |
|                                                       |
|                                                       |
=========================================================
'''
    )
file = open('domainlist.txt','r')
def gstatus(x):
  try:
   s_code = requests.get('https://'+x)
   print(x, s_code.status_code)
  except:
   print("Not resolved: " +x)
   pass
for x in file:
  x = x.strip()
  time.sleep(0.0)
  threading.Thread(target=gstatus, args=(x,)).start()
