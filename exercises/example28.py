i = 0 
numbers = []


def loop(number):
        global i
        #i = 0
        #number = []
        while i < number:
            print "At the top of i is %d" % i
            numbers.append(i)

            i = i + 1
            print "Numbers now: ", numbers
            print "At the bottom i is %d" % i

        print "The numbers: "

        for num in numbers:
            print num

loop(7)