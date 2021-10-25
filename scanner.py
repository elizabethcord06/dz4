import socket
from threading import Thread

N = 2**16 - 1

for port in range(1,100):
    sock = socket.socket()
    try:
        print(port)
        sock.connect(('127.0.0.1', port))
        print("Port", i, "open")
    except:
        continue
    finally:
        sock.close()
