# Author=Rishit Dagli
# License = Apache Licence 2.0
# This program demonstrates a Port scanner built using Python 3.x
# Note: Port scanning is dangerous, so you are advised to not to use 
#       this script without permission

from socket import *
import time

startTime = time.time()

def get_host(target):
	'''
	@author=Rishit Dagli
	Get the IP from the host
	'''

	t_IP = gethostbyname(target)
	return t_IP

def scan(target_IP):
	'''
	
	'''

	print ('Starting scan on host: ', target_IP)
   
		for i in range(50, 500):
	      sock = socket(AF_INET, SOCK_STREAM)
	      
	      conn = sock.connect_ex((target_IP, i))
	      if(conn == 0) :
	         print ('Port %d: open' % (i,))

	      sock.close()
	print('Time taken:', time.time() - startTime)

if __name__ == '__main__':

   target = input('Enter the host to be scanned: ')
   t_IP=get_host(target=target)
   scan(target_IP=t_IP)
	