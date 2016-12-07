import arcade.key
from time import time 
from random import randint

class life:
	def __init__(self, world):
		self.lifes = 3

	def loseLife(self):
		self.lifes -= 1

	def update(self):
		if(self.lifes == 0):
			print("game over")

class Question:
	def __init__(self, world):
		self.world = world
		self.rand_type = randint(0,1)
		self.rand_direction = randint(0,3)
		self.rand_color = randint(0,3)

		self.questionRnd = [self.rand_color,self.rand_direction]

		print("init"+str(self.questionRnd[self.rand_type]))
	
	def checkAns(self, choice):
		print(self.questionRnd[self.rand_type])
		print("choice"+str(choice))
		if(self.questionRnd[self.rand_type] == choice):
			self.world.score += 10;
			print(self.world.score)
		else:
			self.world.life.loseLife()
		self.renewQ()

	def renewQ(self):
		self.rand_type = randint(0,1)
		self.rand_direction = randint(0,3)
		self.rand_color = randint(0,3)

		self.questionRnd = [self.rand_color,self.rand_direction]
		
		print("type"+str(self.rand_type))
		print("init"+str(self.questionRnd[self.rand_type]))

class World:
	def __init__(self, width, height):
		self.question = Question(self)
		self.score = 0
		self.life = life(self)
		self.markedTime = time()

	def on_key_press(self, key, modifiers):
		if key == arcade.key.UP:
			self.question.checkAns(2)
		elif key == arcade.key.DOWN:
			self.question.checkAns(1)
		elif key == arcade.key.LEFT:
			self.question.checkAns(0)
		elif key == arcade.key.RIGHT:
			self.question.checkAns(3)

	def animate(self, delta):
		self.life.update()
		if(time() - self.markedTime >=3):
			self.markedTime = time()
			self.question.renewQ()
