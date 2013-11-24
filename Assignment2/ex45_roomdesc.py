from random import randint
from sys import exit

class Room(object):
        def enter(self):
                exit(1)

class cave_entrance(Room):
	def enter(self):
		print "%s, you are about to face three challenges in the rooms ahead" % p.name
		print "You will face great danger, but the reward is great."
		
		decision = raw_input("\nWould you like to give up or continue? ")		

		if decision == "give up":
			print "%s, how can you give up already? Disappointing" % p.name
			return exit(1)
		else: 
			print "You are either brave or foolish!"
			print "Good luck, you will definately need it."
			return 'room1'

class room1(Room):
	def enter(self):
		print "\nAs you take on the first of three challenges"
		print "You face the first of the Ogre brothers, prepare yourself."
		print "He has a riddle for you:"
		print "What has roots as nobody sees,"
        print "Is taller than trees,"
        print "Up, up it goes,"
        print "And yet never grows? "	
			
	action = raw_input("What is the answer, or do you give up? ")
		
		if answer == "mountain":
			print "%s, you are correct!" % p.name
			print "I will let you pass, you will not be as lucky next time."
			return 'room2'
		elif answer == "give up":
			return 'dead'
		else:
			return 'room1'	

class room2(Room):
	def enter(self):
		print "\nAs you take on the second of three challenges"
		print "You face the second of the Ogre brothers, prepare yourself."
		print "Ogre: You were lucky the last time, but you will not pass me!"
		print "Guess which number I am thinking of between 1-10, if you're"
		print "mistaken. I will kill you!!!!"
			
		answer = raw_input("What number am I thinking of? or do you give up? ")
		
		number = randint(1,10)
		
		if answer == number:
			print "%s, you are correct yet again!" % p.name
			print "Once again you will continue to the next challenge."
			return 'room3'
		elif answer == "give up":
			return 'dead'
		else:
			return 'room2'
	
class room4(Room):
	def enter(self):
		print "\nAs you take on the last of three challenges"
		print "You face the third of the Ogre brothers, prepare yourself."
		print "Ogre: Welcome, ready for your last challenge?"
		print "Your last challenge is to survice a punch from me in the face."
		
		answer = raw_input("Are you ready or do you want to give up?")
		
		punch = randint(0,20)
		
		if answer == "ready":
			print "You tighten as the ogre punches for you."
			if punch > p.health:
				print "You get a fatal blow to the face"
			else:
				print "You survived! Impressive"
				print "Go on to the next room, you have deserved it"
				return 'finish'
		elif answer == "give up":
			return 'dead'
		else: return 'room4'
			
		
		
		
class finish(Room):
	print "As you enter the room you see cake."
	print "ITS CAKE!!!"
	print "CONGRATULATIONS, YOU ARE THE VICTOR!"
	return exit(1)


class dead(Room):
	def giveup(self):
		print "You're dead, you were not able to pass the challenges."
		return exit(1)
			
