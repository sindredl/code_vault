from sys import argv

script, filename = argv

# Here the variable txt is set to open a txt a file within it and store its content in the variable.
txt = open(filename)

# Python uses a method which extends on the variable as seen here called read.
print "Here is your file %r:" % filename
print txt.read()

txt.close()

print "Type the filename again:"
file_again = raw_input("> ")


txt_again = open(file_again)

# the raw input is passed into a variable which a file is identified. Where the a method is used and print the content.
print txt_again.read()

txt_again.close()
