# Class to deal with sockets
import os
import sys
import time
import socket 
from cmd import commandproc

class dsockets:

	def __init(self):
		self.s = socket.socket()         # Create a socket object
		self.host = socket.gethostname() # Get local machine name
		self.port = 12345                # Reserve a port for your service.
		self.s.bind((host, port)) 		# Bind to the port

	def create(self):
		self.s.listen(5)                 # Now wait for client connection.
		while True:
		   c, addr = s.accept()     # Establish connection with client.
		   print ("Got connection from % ") % addr

		   # TODO: Spawn a new thread and pass this socket object to that thread
		   # It will deal with it and send back reply

		   # read certain information from incoming message to pass to command proc


		   time.sleep(1)

	  def destroy(self):
	  	self.s.close()