'''
TCPscan 1.0.0:

A python code to demonstrate demonstrates a TCP scan built using Python 3.x
Note: TCP scan is dangerous, so you are advised to not to use 
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
from datetime import datetime
net = input("Enter the IP address: ")
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1
t1 = datetime.now()

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,135))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
         print (addr , "is live")
         
run1()

t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: " , total)
