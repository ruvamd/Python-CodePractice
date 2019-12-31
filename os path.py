import os
from os import path 
import datetime
from datetime import date,time,timedelta
import time

def main():
    print(os.name)
    print('item exists: '+str(path.exists('textfile.txt')))
    print('item is a file: '+str(path.isfile('textfile.txt')))
    print('item is a directory: '+str(path.isdir('textfile.txt')))
    print('item path and name: '+str(path.split(path.realpath('textfile.txt')))) 
    t=time.ctime(path.getmtime('textfile.txt'))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime('textfile.txt')))
    td=datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime('textfile.txt'))
    print('it has been '+str(td)+' since the file was modified')
    print('or, '+str(td.total_seconds())+' seconds')

main()
