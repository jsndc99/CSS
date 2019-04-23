import socket

s = socket.socket()

n = 105
g = 7
p = 6

A = (g**p)%n

host = socket.gethostname()

port = 10110

s.connect((host,port))

s.send(str(A))

B = s.recv(1024)
B = int(B)

Akey = (B**p)%n

print "A key is "
print Akey

s.close()

