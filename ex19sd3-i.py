# define function cheese_and_crackers

def cheese_splitter(cheese_count, boxes_of_crackers):
	
	print "You have %i cheeses!" % cheese_count
	print "You have %i boxes of crackers!" % boxes_of_crackers
	print "That's enough for a party!"
	print "Get a blanket.\n"

print "How many cheeses do we have?"
amount_of_cheese = raw_input("> ")
cheese = int(amount_of_cheese)

print "How many boxes of crackers do we have?"
amount_of_crackers = raw_input("> ")
crackers = int(amount_of_crackers)

cheese_splitter(cheese, crackers)

#print "We can just give the function numbers directly:"
#cheese_and_crackers(20, 30)
#
#print "OR, we can use variables from our script:"
#amount_of_cheese = 10
#amount_of_crackers = 50
#
#cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
#print "We can even do math inside too:"
#cheese_and_crackers(10 + 20, 5 + 6)
#
#print "And we can combine the two, variables and math:"
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
