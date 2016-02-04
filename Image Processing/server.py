
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 15559
#host = "10.15.59.6"
x = 0
y = 0
kill = False

def setup():
	s.bind((host,port))


def send(x, y):
	s.listen(5)
	c, ref = s.accept()
	cx = str(x)
	cy = str(y)
	newline = "\n"
	sx = cx + newline
	c.send(sx)
	c.send(cy)

def receive():
	s.listen(5)
	c, ref = s.accept()
	killCode = c.recv()


def isKill():
	if(killCode == "true"):
		kill = True
	return kill

	

def close():
	c.close()
	sys.exit()
	


