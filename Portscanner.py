'''
Port Scanner 1.0.0:

A python code to demonstrate demonstrates a Port scanner built using Python 3.x
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

from socket import *
import time

# Calculate time
startTime = time.time()

def get_host(target):
	'''
	@author = "Rishit Dagli"
	Get the IP from the host
	'''

	t_IP = gethostbyname(target)
	return t_IP

def scan(target_IP):
	'''
	@author = "Rishit Dagli"
	Start scanning the host
	'''

	print ('Starting scan on host: ', target_IP)

	for i in range(50, 500):
      
		s = socket(AF_INET, SOCK_STREAM)
      
		conn = s.connect_ex((t_IP, i))
		if(conn == 0) :
			print ('Port %d: OPEN' % (i,))
		s.close()

target = input('Enter the host to be scanned: ')
t_IP=get_host(target=target)
scan(target_IP=t_IP)

# print("functions- get_host, scan")
# print(Docs:)
# print(get_host.__doc__)
# print(scan.__doc__)
