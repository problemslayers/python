# What's the difference between argv and raw_input()?
# The different has to do with where the user is required to give input. If 
# they give your script inputs on the command line, then you use argv. If you 
# want them to input using the keyboard while the script is running, then use 
# raw_input().
#
# this is an import. add features from python feature set

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

age = raw_input("How old are you? ")

