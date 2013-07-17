# What's the difference between argv and raw_input()?
#
# The different has to do with where the user is required to give input. If 
# they give your script inputs on the command line, then you use argv. If you 
# want them to input using the keyboard while the script is running, then use 
# raw_input().

# import the sys module

from sys import argv

# unpack argv and assign it to all of the variables on the left in order

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
