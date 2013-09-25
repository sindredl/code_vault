from random import randint

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Decides the parameters of the function, instead of giving a variable.
# The function is given to integers to use.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


"""
The function is given input through defined variables
which results in 10 and 50 instead of the earlier 20 and 30
"""
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Function is used
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Just a complicated way of passing input, simply saying 30 and 11.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


#Same thing as earlier, 10 + 100 and 50 + 1000
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

coined = randint(2,8)

def function_ex(coins):
	print "Have you counted all your coins?!"
	print "So far you've got %s coins!" % coins
	print "Are you happy with that?"
	yesno = raw_input("Are you? ")	
	
function_ex(coined)