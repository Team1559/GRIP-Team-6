
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
host = "10.15.59.6" #address of server
port = 15559

s.connect((host, port))
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)
s.close
