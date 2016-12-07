import arcade.key

from random import randint

class Question:
	def __init__(self, world):
		self.rand_type = randint(0,1)
		self.rand_direction = randint(0,3)
		self.rand_color = randint(0,3)

		print("A")
		self.questionRnd = [self.rand_color,self.rand_direction]

	def checkAns(self, choice):
		if(self.questionRnd[self.rand_type] == choice):
			print("correct")
		else:
			print ("wrong")

class World:
	def __init__(self, width, height):
		self.question = Question(self)

	def on_key_press(self, key, modifiers):
		if key == arcade.key.UP:
			self.question.checkAns(2)
		elif key == arcade.key.DOWN:
			self.question.checkAns(1)
		elif key == arcade.key.LEFT:
			self.question.checkAns(0)
		elif key == arcade.key.RIGHT:
			self.question.checkAns(3)


