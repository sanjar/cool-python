import socket
from timeit import timeit

class Resolver:

    def __init__(self):
        self._cache={}
        print('Cache is set')

    def __call__(self,host):
        if host not in self._cache:
            self._cache[host]=socket.gethostbyname(host)
        print("%s %s" % ("ww", "eee"))
        print("host ip of %s is %s" %(host, self._cache[host]))

    def timeit(self,statement):
        t = timeit(setup="from __main__ import r" , stmt=statement,number=1)
        print(t)

    def clear(self):
        self._cache.clear()
        
    def printMe(str):
        """This is a docstring, used for documenting. help(resolver to see the document)
        
        Args:
            str: Any string which you want to print.
        """
        print(str)

    #print(__name__)
    
    if __name__ == '__main__':
        printMe('this is life')
