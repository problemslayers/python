# import argv and exists

from sys import argv
from os.path import exists

# expect the file we want to copy, and the file we want to copy to

script, from_file, to_file = argv

# 

in_file = open(from_file)
indata = in_file.read()

# 

out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()
in_file.close()
