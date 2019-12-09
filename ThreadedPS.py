'''
Threaded Port Scanner 1.0.0:

A python code to demonstrate demonstrates a Threaded Port scanner built using Python 3.x
We here use threading to speed up the process
Note: Port scanning is dangerous, so you are advised to not to use 
     this script without permission
'''

__author__ = "Rishit Dagli"
__copyright__ = ""
__credits__ = ["Rishit Dagli"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Rishit Dagli"
__email__ = "rishit.dagli@gmail.com"
__status__ = "Development"

import socket
import time
import threading
from queue import Queue

# set Timeout time
socket.setdefaulttimeout(0.25)

print_lock = threading.Lock()

target = input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print ('Starting scan on host: ', t_IP)

def portscan(port):
   '''
   @author = "Rishit Dagli"
   scan for ports
   '''

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'is open')
      con.close()
   except:
      pass

def threader():
   '''
   @author = "Rishit Dagli"
   Do the portscan in a threads
   '''

   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 500):
   q.put(worker)

# Join the results from threads   
q.join()

# Print time taken
print('Time taken:', time.time() - startTime)

# print("functions- portscan, threader")
# print(Docs:)
# print(portscan.__doc__)
# print(threader.__doc__)
