# Imports randint from the random module making it possible to generate a random integer.
from random import randint


class Adventurer:
	def __init__(self):
		self.name = ""
		self.health = 1
		self.max_health = 1
	
	def damage(self, foe):
		damage = min(
			max(randint(0, self.health) - randint(0, foe.health), 0),
			foe.health)
		foe.health = foe.health - damage
		if damage == 0: print "%s blocks %s's attack!" % (foe.name, self.name)
		else: print "%s hits %s!" % (self.name, foe.name)
		return foe.health <= 0

class Foe(Adventurer):
	def __init__(self, player):
		Adventurer.__init__(self)
		self.name = "Sindre Dahl Loken"
		self.health = randint(1, player.health)

class Player(Adventurer):

	def __init__(self):
		Adventurer.__init__(self)
		self.state = "regular"
		self.health = 10
		self.health_max = 10
	
	def leave(self):
		print "%s takes the easy way out and lay down to die.\nEmbarrassing." % self.name
	
	def help(self): print Actions.keys()
	
	def status(self): print "%s's current health: %d/%d" % (self.name, self.health, self.max_health)
	
	def explore(self):
		if self.state != "regular":
			print "%s concentrate on the fight!" % self.name
			self.foe_attacks()
		else:
			print "%s ventures into the dark abyss." % self.name
			if randint(0, 1):
				self.foe = Foe(self)
				print "A %s jumps up from nowhere!" % self.foe.name
				self.state = "battle"
	
	def hide(self):
		if self.state != "fight": print "There is nothing to hide from, %s it's time to explore!" % self.name
		else:
			if randint(1, self.health + 5) > randint(1, self.foe.health):
				print "%s disappears and %s moves on." % (self.name, self.foe.name)
				self.foe = None
				self.state = "regular"
			else: print "%s tried to hide, but %s found you!" (self.name, self.foe.name)
	
	def sleep(self):
		if self.state != "regular": print "%s you're in the middle of a god damn fight!" % self.name
		else:
			print "%s gets some sleep." % self.name
			if randint(0, 1):
				self.foe = Foe(self)
				print "%s drops down on you screaming like mad!" % self.foe.name
				self.state = "battle"
				self.foe_attacks()
	
	def attack(self):
		if self.state != "battle": print "%s swings around him furiously, but there's no one there." % self.name
		else:
			if self.damage(self.foe):
				print "%s head was chopped straight off!" % self.foe.name
				self.foe = None
				self.state = "regular"
				if randint(0, self.health) < 10:
					self.health = self.health + 1
					self.health_max = self.health_max + 1
					print "%s grows stronger!" % self.name
				else: self.foe_attacks()
	
	def foe_attacks(self):
		if self.foe.damage(self): print "%s was easily slain by %s! :-(\n Just terrible" % (self.name, self.foe.name)
			
	
# A dictionary mapping the different actions to functions within the player class.
Actions = {
  'leave': Player.leave,
  'help': Player.help,
  'status': Player.status,
  'sleep': Player.sleep,
  'explore': Player.explore,
  'hide': Player.hide,
  'attack': Player.attack,
  }
		
p = Player()
p.name = raw_input("\nWhat's your name adventurer? ")
print ">> type help to get a list of actions <<\n"
print "%s enters a dark cavern, looking for treasure." % p.name

while(p.health > 0):
  line = raw_input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Actions.keys():
      if args[0] == c[:len(args[0])]:
        Actions[c](p)
        commandFound = True
        break
    if not commandFound:
      print "%s that's an incorrect command." % p.name