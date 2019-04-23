import numpy as np
import socket as sk
import re
import struct
import time

print("Enter message")
plain_text = input()
# Pad PT if small
padding = len(plain_text)%3
if padding != 0:
    plain_text = plain_text+('x'*(padding-1))
    print ('padded plain text = '+plain_text)
# Split PT in sets
pairs = re.findall('...',plain_text)
print('Sets after splitting = ',pairs)
# Put Characters into matrices
equationOne_String = pairs[0]
equationTwo_String = pairs[1]
equationOne_LHS = [ord(equationOne_String[0])-96,ord(equationOne_String[1])-96]
equationTwo_LHS = [ord(equationTwo_String[0])-96,ord(equationTwo_String[1])-96]
equationOne_RHS = ord(equationOne_String[2])-96
equationTwo_RHS = ord(equationTwo_String[2])-96
matrix_LHS = np.array([equationOne_LHS,equationTwo_LHS])
matrix_RHS = np.array([equationOne_RHS,equationTwo_RHS])
# Solve Simultaneous equations
simul_output = np.linalg.solve(matrix_LHS,matrix_RHS)
X_Value = simul_output[0]%26
Y_Value = simul_output[1]%26
# Calculate Key
key = (X_Value+Y_Value)%26
print ('Key is ',key)
# Encrypt
cipher_text = []
for x in plain_text:
    cipher_text.append(chr(ord(x)^int(key)))
cipher_text_final = ''
cipher_text_final =  cipher_text_final.join(cipher_text)
print (cipher_text)
print (cipher_text_final)
# Send Cipher Text and Key
s = sk.socket()
host = sk.gethostname()
port = 12345
s.connect((host,port))
key = int(key)
s.send(str(key).encode())
time.sleep(1)
s.send(cipher_text_final.encode())
s.close()







