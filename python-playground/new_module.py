def found():
    print("yes, it is found")

import socket
def trySocket(host):
    """its a document"""
    print("test")
    try:
        print(socket.gethostbyname(host))
    except:
        print("error")
