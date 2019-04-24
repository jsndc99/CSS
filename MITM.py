import socket
import time

def AliceMITM():
	# Pretends to be bob
	print "Pretends to be bob"
	s = socket.socket()

	host = socket.gethostname()

	port = 10110
	
	n = 105
	g = 7
	p = 3
	
	B = (g**p)%n

	s.bind((host,port))
	
	s.listen(5)
	
	conn,addr = s.accept()
	
	A = conn.recv(1024)
	A = float(A)
	
	conn.send(str(B))
	
	Bkey = (A**p)%n
	
	print "Key between Alice and MITM(bob)"
	print Bkey

def BobMITM():
	# Pretends to be Aice
	print "Pretends to be Alice"
	s = socket.socket()

	host = socket.gethostname()

	port = 10111
	
	n = 105
	g = 7
	p = 4
	
	A = (g**p)%n

	s.connect((host,port))
	
	s.send(str(A))
	
	B = s.recv(1024)
	B = float(B)
	
	Akey = (B**p)%n
	
	print "Key between Bob and MITM(A)"
	print Akey
	

AliceMITM()
BobMITM()
	


