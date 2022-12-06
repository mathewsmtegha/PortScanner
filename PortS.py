#!/usr/bin/env python3
import socket
# We import the ipaddress module. We want to use the ipaddress.ip_address(address)
# method to see if we can instantiate a valid ip address to test.
import ipaddress
# We need to create regular expressions to ensure that the input is correctly formatted.
import re
import time
startime = time.time()

# Regular Expression Pattern to extract the number of ports you want to scan.
# You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
# Once you've successfully connected a port is seen as open.
open_ports = []
# Ask user to input the ip address they want to scan.
while True:
 ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
 # If we enter an invalid ip address the try except block will go to the except block and say you entered an invalid ip address.
 try:
  ip_address_obj = ipaddress.ip_address(ip_add_entered)
  # The following line will only execute if the ip is valid.
  print("You entered a valid ip address.")
  break
 except:
  print("You entered an invalid ip address")

while True:
 # You can scan 0-65535 ports.
 # the ports is not advised.
 print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 20-443)")
 port_range = input("Enter port range: ")
 print("Starting scan on host.......... ")
 port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
 if port_range_valid:
  port_min = int(port_range_valid.group(1))
  port_max = int(port_range_valid.group(2))
  break

# Basic socket port scanning
for port in range(port_min, port_max + 1):
 try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.settimeout(0.5)
   # We use the socket object we created to connect to the ip address we entered and the port number.
   s.connect((ip_add_entered, port))
   # If the following line runs then then it was successful in connecting to the port.
   open_ports.append(port)

 except:
  pass

for port in open_ports:
 print(f"Port {port} is open on {ip_add_entered}.")

print("time taken: ", time.time() - startime)

