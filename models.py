import arcade.key

from random import randint

class Question:
	def __init__(self, world):
		self.world = world
		self.rand_type = randint(0,1)
		self.rand_direction = randint(0,3)
		self.rand_color = randint(0,3)

		self.questionRnd = [self.rand_color,self.rand_direction]

	def checkAns(self, choice):
		if(self.questionRnd[self.rand_type] == choice):
			self.world.score += 10;
			print(self.world.score)
		else:
			print ("wrong")
		self.renewQ()

	def renewQ(self):
		self.rand_type = randint(0,1)
		self.rand_direction = randint(0,3)
		self.rand_color = randint(0,3)

		self.questionRnd = [self.rand_color,self.rand_direction]
		

class World:
	def __init__(self, width, height):
		self.question = Question(self)
		self.score = 0
	
	def on_key_press(self, key, modifiers):
		if key == arcade.key.UP:
			self.question.checkAns(2)
		elif key == arcade.key.DOWN:
			self.question.checkAns(1)
		elif key == arcade.key.LEFT:
			self.question.checkAns(0)
		elif key == arcade.key.RIGHT:
			self.question.checkAns(3)


