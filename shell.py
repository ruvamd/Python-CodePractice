import os
from os import path
import shutil
from shutil import make_archive

def main():
  if path.exists('textfile.txt'):
      src=path.realpath('textfile.txt')
      dst=src+'.bak'
      #shutil.copy(src,dst)
      #shutil.copystat(src,dst)
      #os.rename('textfile.txt','newfile.txt')
      root_dir,tail=path.split(src)
      shutil.make_archive('archive','tar',root_dir)
main()     