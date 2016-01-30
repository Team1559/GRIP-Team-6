
import numpy as np
import socket
import sys

x = "hello"
y = "it's me \n"
a = "I was wondering \n"
b = "If after all these years \n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 15559
host = socket.gethostname()
#host = "127.0.0.1"
s.bind((host, port))

s.listen(5)
while True:
    c, ad = s.accept()
    c.send(x)
    c.send(y)
    c.send(a)
    c.send(b)
    c.close
    sys.exit()
