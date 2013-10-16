class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_it(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
			"I don't want to get sued",
			"So I'll stop right there"])
			
bulls_on_parade = Song(["They rally around the familiy",
						"With pockets full of shells"])
						
song_a_dilly_doo = Song(["I am so bored, so so bored",
						"Please mister, entertain me. uauaaua"])
		

song1 = "This is a great great song, a variable song"

print Song(song1)
		
happy_bday.sing_it()

bulls_on_parade.sing_it()

song_a_dilly_doo.sing_it()
			