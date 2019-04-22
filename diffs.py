import socket
import sys
import traceback
from threading import Thread

def start_server():
    host = "127.0.0.1"
    port = 8888         # arbitrary non-privileged port
    y = 9               # receiver's private key
    g,n = 7,11
    print '******* Prime Numbers decided : ',g,' , ',n,'*******'
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
    print("Socket created")

    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()
    B = str((g**y)%n)
    soc.listen(5)       # queue up to 5 requests
    print("Socket now listening")

    # infinite loop- do not reset for every requests
    connection, address = soc.accept()
    ip, port = str(address[0]), str(address[1])
    print("Connected with " + ip + ":" + port)
    try:
        Thread(target=client_thread, args=(connection, ip, port,B)).start()
    except:
        print("Thread did not start.")
        traceback.print_exc()
    soc.close()


def client_thread(connection, ip, port, B, max_buffer_size = 5120):
    client_input = receive_input(connection, max_buffer_size)
    if "--QUIT--" in client_input:
        print("Client is requesting to quit")
        connection.close()
        print("Connection " + ip + ":" + port + " closed")
        is_active = False
    else:
        print 'Computed B : ',B
        temp = raw_input('Sending B...')
        connection.sendall(B.encode("utf8"))
        print 'Send successful!'

def receive_input(connection, max_buffer_size):
    y = 9               # receiver's private key
    g,n = 7,11
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))
    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    A = int(decoded_input)
    print 'Received : ',decoded_input
    print 'Shared key k1 : ',(A**y)%n
    return str(A)

start_server()

''' ************************ OUTPUT ****************************
******* Prime Numbers decided :  7  ,  11 *******
Socket created
Socket now listening
Connected with 127.0.0.1:42230
Received :  2
Shared key k1 :  6
Computed B :  8
Sending B...
Send successful!
'''
