def numb(a, b):
	for n in range(a, b):
		print "At the top i is %d" % n
		numbers.append(n)
	
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % n

numbers = []
numb(2, 8)

print "The numbers: "

for num in numbers:
	print num
