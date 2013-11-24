import ex45_roomdesc

class Adventurer:
	def __init__(self):
		self.name = ""
		self.health = 1
		self.max_health = 1
					
class Player(Adventurer):

	def __init__(self):
		Adventurer.__init__(self)
		self.health = 10
		self.health_max = 10
	
	def help(self): print Actions.keys()
	
	def status(self): print "%s's current health: %d/%d" % (self.name, self.health, self.max_health)
  
  
class Engine(object):

    def __init__(self, room_o):
        self.room_o = room_o

    def play(self):
        c_room = self.room_o.first_room()

        while True:
            print "\n--------"
            nx_rooms = c_room.enter()
            c_room = self.room_o.room_nx(nx_rooms)
                        
class Overview(object):

    room = {
		'cave_entrance' : ex45_roomdesc.cave_entrance(),
        'room1': ex45_roomdesc.room1(),
        'room2': ex45_roomdesc.room2(),
        'room3': ex45_roomdesc.room3(),
        'finish': ex45_roomdesc.finish(),
		'dead': ex45_roomdesc.dead()
    }

    def __init__(self, room_start):
        self.room_start = room_start

    def room_nx(self, room_name):
        return Overview.room.get(room_name)

    def first_room(self):
        return self.room_nx(self.room_start)  
  
  

p = Player()
p.name = raw_input("\nWhat's your name adventurer? ")
ooverview = Overview ('cave_entrance')
v_game = Engine(ooverview)
v_game.play()
