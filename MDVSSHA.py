import hashlib as hl
import time
def MD5():
    f = open('text.txt','rb')
    contents = f.read()


    start = time.time()

    #print contents

    x = hl.md5(contents)

    print x.digest()

    stop = time.time()

    time_taken = start-stop

    print time_taken

def SHA():
    f = open('text.txt','rb')
    contents = f.read()


    start = time.time()

    #print contents

    x = hl.sha1(contents)

    print x.digest()

    stop = time.time()

    time_taken = start-stop

    print time_taken

MD5()
SHA()