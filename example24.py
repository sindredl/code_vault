people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
	# If the variable cars is higher than people it will print we should take the cars, which is the result here.
elif cars < people:
    print "We should not take the cars."
	# if cars are less than people print the string above.
else:
	# if the answer is none of the above, they are equal each other print the string below
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."+
	