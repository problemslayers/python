# import argv

from sys import argv

# expect a file name

script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^c)."
print "If you do want that, hit RETURN."

# prompt for input

raw_input("?")
print "Opening the file..."

# truncate and set target

target = open(filename, 'w+')
print "Truncating the file.  Goodbye!"

# empty target
#
#target.truncate()
print "Now I'm going to ask you for three lines."

# fill 3 lines - a 3 line text editor

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."

# write lines to file

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write("line1\nline2\nline3")
print "And finally, we close it."

# close the file

target.close()
