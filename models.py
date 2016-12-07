import arcade.key

from random import randint

class Question:
	def __init__(self, world):
		self.rand_type = randint(0,1)
		self.rand_direction = randint(0,3)
		self.rand_color = randint(0,3)

		self.questionRnd = [self.rand_color,self.rand_direction]

class World:
	def __init__(self, width, height):
		self.question = Question(self)

#	def on_key_press(self, key, modifiers):
#		if key == arcade.key.UP:
#			checkAns()
#		elif key == arcade.key.DOWN:

#		elif key == arcade.key.LEFT:

#		elif key == arcade.key.RIGHT:
	


