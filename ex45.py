""" Make a game, use more than one file using imports,
use one class per room"""

# print You wake up in a room, it's pitch black what do you do?
# Present options - Search - Jump - Give up.

# If search, you find a switch, the whole room lights up as you seemingly find the light switch. You are in a room underground with three avaibable passages.
# Pick number one, two or three?

#If Jump, you jump but nothing happens what did you expect?

# If give up, you give up and end up never seeing the light of day again.


# PASSAGE ONE its a dead end, what do you do?
# Search wall or turn back? If search wall a cage drops on top of you as you activate some kind of hidden lever. The cage is unbreakable and 
# you die a long and painful death.


# PASSAGE TWO, the new passages leads to a new room with some crates what do you do?
# Break crate or turn back.

#If you brake crate you find a key. - Turn back?
# If you turn back, as you turn you face a huge hairy naked man foaming from his mouth seemingly ready to attack you.
# If crate broken - try to run past. The man catches you, throws you to the ground as he strangles you. The last thing you see is his hairy belly.

#If crate is not broken, as you turn you face a huge hairy naked man foaming from his mouth seemingly ready to attack you.
# Try to run or throw crate. If run same scenario as above. If Throw crate, you hit him straight in the face as he drops to the ground, inside the crate
# a key falls out you pick it up as you return to the previous room.

# PASSAGE THREE
# You reach the end of the passage with a set of stairs leading up to a door in the ceiling
# IF KEY, UNLOCK OR TURN BACK? You unlock the door, open it and sunlight blinds you instantly it takes you a second to recover before you escape.
# NO KEY, Hit door or turn back. If you hit door, you feel the whole cave shaking before it crumbles ontop of you.


print "You are dazed and confused as you wake up in a pitch black room. What do you do next?"

def first_choice():
	print ("#SEARCH, #JUMP, #GIVE UP")
	

	
first_choice()
choice = raw_input("> ")

if choice == "search":
	print "\n You find a switch, the whole room lights up as you seemingly find the light switch. You are in a room underground with three available passages."
	print "Which passage do you decide to go down?"
	print "#ONE, #TWO, #THREE"
elif choice == "jump":
	 print "You jump, but nothing happens what did you expect?"
	 first_choice()
	 choice = raw_input("> ")
elif choice == "give up":
	print "You give up, as darkness engulfs you."
else:
	print "You didn't pick an option and is left with no options as nothing happens."

