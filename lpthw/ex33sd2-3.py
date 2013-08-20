def numb(i, n, c):
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + c
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

numbers = []
numb(3, 8, 2)

print "The numbers: "

for num in numbers:
	print num
