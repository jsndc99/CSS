import socket

s = socket.socket()

host = socket.gethostname()

port = 10111

n = 105
g = 7
p = 8

B = (g**p)%n

s.bind((host,port))

s.listen(5)

c, addr = s.accept()

A = c.recv(1024)

A = float(A)

Bkey = (A**p)%n

print "B key is "
print Bkey

c.send(str(B))

s.close()
