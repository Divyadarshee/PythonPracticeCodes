import sys
import os

filename = sys.argv[1]

if not os.path.exists(filename):
  with open(filename, 'w'):
    f.write("New File created\n")
else:
  print("Error, the file {} already exists!".format(filename))
  sys.exit(1)
