import os, sys

def remove_file(filename):
   path = os.path.realpath(filename)
   print(path)
   os.remove(path)

remove_file(sys.argv[1])
