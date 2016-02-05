
import socket
import sys

port = 15559
host = "10.15.59.6" #good fix n8


class Server(object):

	def __init__(self):

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.setblocking(0)
		#host = socket.gethostname()
		self.s.bind((host,port))
		self.s.listen(5)


	def send(self, x, y):
		if self.c == None:
			return
		try:	
			self.c.send("X Value: %d\n" % x)
			self.c.send("Y Value: %d\n" % y)
		except socket.error:
			pass


	def receive(self):
		if self.c == None:
			return
		try:
			r = self.c.recv(1024)
			print r
			return r
		except socket.error:
			pass


	def accept(self):
		try:
			self.c, ref = self.s.accept()
		except socket.error:
			self.c = None
	

	def close(self):
		if self.c == None:
			return
		self.c.close()
	


