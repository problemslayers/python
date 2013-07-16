# x (str) is "There are 10 types of people."
x = "There are %d types of people." % 10
# binary (str) is "binary"
binary = "binary"
# do_not (str) is "don't"
do_not = "don't"
# y (str) is "Those who know binary and those who don't."
y = "Those who know %s and those who %s." % (binary, do_not)
# print x, on a new line print y
print x
print y
# print "I said: 'There are %d types of people.'."
print "I said: %r." % x
# print "I also said: 'Those who know binary and those who don't.'."
print "I also said: '%s'." % y
# hilarious (str) is "False"
hilarious = False
# joke_evaluation is "Isn't that joke so funny?! False"
joke_evaluation = "Isn't that joke so funny?! %r"
# print "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
