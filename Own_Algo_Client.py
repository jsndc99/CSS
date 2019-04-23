import socket as sk
import struct
import time
# key will be encrypted using another key sent by diffie hellman
# for this example , key will be sent directly
s = sk.socket()
host = sk.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)
c, addr = s.accept()
#Receive key
key = c.recv(1024)
key = int(key)
print(key)
# Delay to receive next packet
time.sleep(1)
# Receive Cipher Text
cipher_text = (c.recv(1024)).decode()
print (cipher_text)

# Decrypt Cipher text
decodedText = []
for y in cipher_text:
    decodedText.append(chr(ord(y)^int(key)))
print (decodedText)
decodedText_final = ''
decodedText_final = decodedText_final.join(decodedText)
print (decodedText_final)
s.close()