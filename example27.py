i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

	
integer = 0	
six = 10
list = []

def while_loop(integer):
	while integer < six:
		print "The current number is %s" % integer
		list.append(integer)
		
		integer = integer + 1
		print "The current number is", integer