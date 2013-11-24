import ex25

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# An error would occur here because there was a colon missing after the bracket.
def print_first_word(words):
	"""Prints the first word after popping it off."""
	# Typo where it is written poop, it should be pop which is a valid option
	word = words.pop(0)
	print word

# Error with the indent
def print_first_word2(words):
    """Prints the first word after popping it off."""
	

# There was a closing bracket missing on line 19, closing in -1.
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 2 - 5
print "This should be five: %s" % five

# A backslash was position the wrong way, \ instead of / causing an error.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# One too many equal signs causes an error.
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
# The variable here was spelled wrong
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# There is a typo in the parameter "Start_pont" and a closing bracket is missing.
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

sentence = "All good things come to those who wait."

# It is needed to import the file to use its functions.
words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
# A full stop was in front of the function causing an error.
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
# Print was typed wrong causing nothing to be printed and an error to occur.
print sorted_words

# Another typo, print_irst_and_last.
print_first_and_last(sentence)
# There was an unexpected indent causing an error, there is also a typo.
print_first_and_last_sorted(sentence)
