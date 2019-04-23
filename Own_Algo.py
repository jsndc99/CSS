import numpy as np
import socket as sk
import re
import struct

print("Enter message")

plain_text = input()

padding = len(plain_text)%3

if padding != 0:
    plain_text = plain_text+('x'*(padding-1))
    print ('padded plain text = '+plain_text)

pairs = re.findall('...',plain_text)

print('Sets after splitting = ',pairs)

equationOne_String = pairs[0]

equationTwo_String = pairs[1]

equationOne_LHS = [ord(equationOne_String[0])-96,ord(equationOne_String[1])-96]

equationTwo_LHS = [ord(equationTwo_String[0])-96,ord(equationTwo_String[1])-96]

equationOne_RHS = ord(equationOne_String[2])-96

equationTwo_RHS = ord(equationTwo_String[2])-96

matrix_LHS = np.array([equationOne_LHS,equationTwo_LHS])

matrix_RHS = np.array([equationOne_RHS,equationTwo_RHS])

simul_output = np.linalg.solve(matrix_LHS,matrix_RHS)

X_Value = simul_output[0]%26

Y_Value = simul_output[1]%26

''''''
print(matrix_LHS)

print(matrix_RHS)

print(X_Value)

print(Y_Value)
''''''

key = (X_Value+Y_Value)%26

print ('Key is ',key)

cipher_text = []

for x in plain_text:
    cipher_text.append(chr(ord(x)^int(key)))

cipher_text_final = ''

cipher_text_final =  cipher_text_final.join(cipher_text)

print (cipher_text)
print (cipher_text_final)

s = sk.socket()

host = sk.gethostname()

port = 12345

s.connect((host,port))

key = int(key)

s.send(str(key).encode())

import time

time.sleep(1)

s.send(cipher_text_final.encode())

s.close()







