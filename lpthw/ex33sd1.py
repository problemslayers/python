def numb(i):
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

numbers = []
n = 8
numb(3)

print "The numbers: "

for num in numbers:
	print num
