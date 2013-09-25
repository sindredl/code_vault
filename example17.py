from sys import argv

# The normal thing, needs an argument when started
script, input_file = argv

# A function is defined with the parameter f, which it will read and print.
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

	
def print_a_line(line_count, f):
    print line_count, f.readline()

# The variable is set to contain the argument passed on from the start.
current_file = open(input_file)

print "First let's print the whole file:\n"
# This function is used and reads everything in the variable current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# This function is used to go back to the files starting position which it can be read again
rewind(current_file)

print "Let's print three lines:"

# Sets the variable to be 1, the prints the line and the linecount.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)