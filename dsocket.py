# Class to deal with sockets
import os
import sys
import time
import socket 
from cmd import commandproc

class dsockets:

	def __init__(self):
		self.s = socket.socket()        # Create a socket object
		host = socket.gethostname() 	# Get local machine name
		port = 12141                	# Reserve a port for your service.
		self.s.bind((host, port)) 		# Bind to the port
		print ("listening to port! host: %s, port: %s ") % (host, port)

	def create(self):
		self.s.listen(5)                # Now wait for client connection.
		while True:
		   c, addr = self.s.accept()    # Establish connection with client.
		   print ("Got connection from %s ") % str(addr)
		   commandproc(c, addr)


	def destroy(self):
	  	self.s.close()