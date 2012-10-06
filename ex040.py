# ex040.py

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song([	"Happy birthday to you",
										"I don't want to get sued",
										"So I'll stop right there"])

bulls_on_parade = Song(["They rally round the family",
												"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

rick_roll = [	"Never going to give you up",
							"Never going to let you down",
							"Never going to run around"]

song2 = [	"Woo-hoo!",
					"Woo-hoo!",
					"Woo-hoo!"]

ace_of_spades = [	"If you like to gamble",
									"I tell you, I'm your man",
									"You win some, lose some"]

very_poor = Song(rick_roll)
blur = Song(song2)
motorhead = Song(ace_of_spades)

very_poor.sing_me_a_song()