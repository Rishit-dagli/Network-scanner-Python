# Network-scanner-Python
A simple network scanner using Python 3.x which demonstrates a basic port scanner, TCP port scanner, Ping Sweep and threaded port scanner
 
## Port scanner
Port scanning may be defined as a surveillance technique, which is used in order to locate the open ports available on a particular host. Network administrator, penetration tester or a hacker can use this technique. We can configure the port scanner according to our requirements to get maximum information from the target system.

Now, consider the information we can get after running the port scan −

* Information about open ports.

* Information about the services running on each port.

* Information about OS and MAC address of the target host.

The 65535 ports can be divided into the following three ranges −

*    System or well-known ports: from 0 to 1023

*    User or registered ports: from 1024 to 49151

*    Dynamic or private ports: all > 49151

When we run the above script, it will prompt for the hostname, you can provide any hostname like name of any website but be careful because port scanning can be seen as, or construed as, a crime. We should never execute a port scanner against any website or IP address without explicit, written permission from the owner of the server or computer that you are targeting. That is why it is advisable to use port scanner on localhost or your own website (if any).
<br><br>
The above script generates the following output −

    Enter the host to be scanned: localhost
    Starting scan on host: 127.0.0.1
    Port 135: OPEN
    Port 445: OPEN
    Time taken: 452.3990001678467

The output shows that in the range of 50 to 500 (as provided in the script), this port scanner found two ports — port 135 and 445, open. We can change this range and can check for other ports.

## Ping sweep

Actually in one or other sense, ping sweep is also known as ping sweeping. The only difference is that ping sweeping is the procedure to find more than one machine availability in specific network range. For example, suppose we want to test a full list of IP addresses then by using the ping scan, i.e., ping command of operating system it would be very time consuming to scan IP addresses one by one. That is why we need to use ping sweep script. Following is a Python script for finding live hosts by using the ping sweep.
<br><br>
The above script works in three parts. It first selects the range of IP address to ping sweep scan by splitting it into parts. This is followed by using the function, which will select command for ping sweeping according to the operating system, and last it is giving the response about the host and time taken for completing the scanning process.
<br>
The above script generates the following output −

    Enter the Network Address: 127.0.0.1
    Enter the Starting Number: 1
    Enter the Last Number: 100

    Scanning in Progress:
    Scanning completed in: 0:00:02.711155

The above output is showing no live ports because the firewall is on and ICMP inbound settings are disabled too. After changing these settings, we can get the list of live ports in the range from 1 to 100 provided in the output.

## TCP scan

To establish a TCP connection, the host must perform a three-way handshake. Follow these steps to perform the action −

Step 1 − Packet with SYN flag set

In this step, the system that is trying to initiate a connection starts with a packet that has the SYN flag set.

Step 2 − Packet with SYN-ACK flag set

In this step, the target system returns a packet with SYN and ACK flag sets.

Step 3 − Packet with ACK flag set

At last, the initiating system will return a packet to the original target system with the ACK flag set.

The above script works in three parts. It selects the range of IP address to ping sweep scan by splitting it into parts. This is followed by using a function for scanning the address, which further uses the socket. Later, it gives the response about the host and time taken for completing the scanning process. The result = s. connect_ex((addr,135)) statement returns an error indicator. The error indicator is 0 if the operation succeeds, otherwise, it is the value of the errno variable. Here, we used port 135; this scanner works for the Windows system. Another port which will work here is 445 (Microsoft-DSActive Directory) and is usually open.
<br>
The above script generates the following output −

    Enter the IP address: 127.0.0.1
    Enter the Starting Number: 1
    Enter the Last Number: 10

    127.0.0.1 is live
    127.0.0.2 is live
    127.0.0.3 is live
    127.0.0.4 is live
    127.0.0.5 is live
    127.0.0.6 is live
    127.0.0.7 is live
    127.0.0.8 is live
    127.0.0.9 is live
    127.0.0.10 is live
    Scanning completed in: 0:00:00.230025

## Threaded port scanner for higher efficiency

As we have seen in the above cases, port scanning can be very slow. For example, you can see the time taken for scanning ports from 50 to 500, while using socket port scanner, is 452.3990001678467. To improve the speed we can use threading.
<br>
In the above script, we need to import the threading module, which is inbuilt in the Python package. We are using the thread locking concept, thread_lock = threading.Lock() to avoid multiple modification at a time. Basically, threading.Lock() will allow single thread to access the variable at a time. Hence, no double modification occurs.

Later, we define one threader() function that will fetch the work (port) from the worker for loop. Then the portscan() method is called to connect to the port and print the result. The port number is passed as parameter. Once the task is completed the q.task_done() method is called.

Now after running the above script, we can see the difference in speed for scanning 50 to 500 ports. It only took 1.3589999675750732 seconds, which is very less than 452.3990001678467, time taken by socket port scanner for scanning the same number of ports of localhost.

The above script generates the following output −

    Enter the host to be scanned: localhost
    Starting scan on host: 127.0.0.1
    135 is open
    445 is open
    Time taken: 1.3589999675750732
