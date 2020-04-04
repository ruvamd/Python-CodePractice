from time import time
from contextlib import contextmanager

header='thes is the header \n'
footer='\n this is the footer \n'

@contextmanager
def newLogFile(name):
    try:
        logname=name
        f=open(logname,'w')
        f.write(header)
        yield f
    finally:
        f.write(footer)
        print 'logfile created'
        f.close()
        
