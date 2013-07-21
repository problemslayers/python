# import argv (argument vector) from sys module

from sys import argv

# unpack argv - the argument we'll be expecting is a filename

script, filename = argv

# we might do this. we don't have to

prompt = "> "

# open the file and put its contents into txt

txt = open(filename)

# print a message with the filename

print "Here's your file %r:" % filename

# give the file txt a read command with the . and print the result

print txt.read()

## another print message
#
#print "Type the filename again:"
#
## ask for input with prompt. put result in file_again
#
file_again = raw_input(prompt)
#
## open the file and put its contents in txt_again
#
#txt_again = open(file_again)
#
## give the file txt_again a read command and print the result
#
#print txt_again.read()
