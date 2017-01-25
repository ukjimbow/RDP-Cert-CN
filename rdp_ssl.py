#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################################
#												 #
# Create a list of IP addresses in hosts.txt 	 #
#												 #
##################################################


import csv
import sys
import socket 
from socket import error as SocketError
import errno

hosts = open('hosts.txt')
c = csv.writer(open("3389_output.csv", "wb"))

for line in hosts:
	line = line.rstrip()
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((line, 3389))
		sslSocket = socket.ssl(s)
		print line + "," + repr(sslSocket.server())
		c.writerow([line + "," + repr(sslSocket.server())])
		s.close()
	except:
		pass

