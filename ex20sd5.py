# import argv

from sys import argv

# expect file name

script, input_file = argv

# this function takes a file name as an argument and prints that file

def print_all(f):
	print f.read()
	
# this function returns the script to the beginning of the file

def rewind(f):
	f.seek(0)
	
# this function prints the line count followed by the contents of the line

def print_a_line(line_count, f):
	print line_count, f.readline()

# open file and put contents in current_file

current_file = open(input_file)
print "First let's print the whole file:\n"

# print the contents of the input file's file descriptor

print_all(current_file)
print "Now let's rewind, kind of like a tape."

# returns read position to beginning of the file

rewind(current_file)
print "Let's print three lines:"

# initialize a new counter current_line

current_line = 1

# print the line number followed by the line

print_a_line(current_line, current_file)

# increment the counter and print the next line

current_line += 1
print_a_line(current_line, current_file)

# increment the counter and print the next line

current_line += 1
print_a_line(current_line, current_file)
