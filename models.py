import arcade.key
from time import time 
from random import randint

class life:
	def __init__(self, world):
		self.lifes = 3
		self.world = world

	def loseLife(self):
		self.lifes -= 1

	def update(self):
		if(self.lifes == 0):
			self.world.canPlay = False

class Question:
	def __init__(self, world):
		self.world = world
		self.newQuestion()
	
	def checkAns(self, choice):
		if(self.questionRnd[self.rand_type] == choice):
			self.world.score += 10;
		else:
			self.world.life.loseLife()
		self.newQuestion()

	def newQuestion(self):
		self.rand_type = randint(0,1)
		self.rand_direction = randint(0,3)
		self.rand_color = randint(0,3)

		self.questionRnd = [self.rand_color,self.rand_direction]
		
		self.world.markedTime = time()

class World:
	def __init__(self, width, height):
		self.question = Question(self)
		self.score = 0
		self.life = life(self)
		self.markedTime = time()
		self.canPlay = True

	def on_key_press(self, key, modifiers):
		if key == arcade.key.UP:
			self.question.checkAns(2)
		elif key == arcade.key.DOWN:
			self.question.checkAns(1)
		elif key == arcade.key.LEFT:
			self.question.checkAns(0)
		elif key == arcade.key.RIGHT:
			self.question.checkAns(3)
		elif(not self.canPlay and key == arcade.key.SPACE):
			self.clear()

	def animate(self, delta):
		self.life.update()
		self.time = time() - self.markedTime
		if(self.time >=3):
			self.markedTime = time()
			self.life.loseLife()
			self.question.newQuestion()
	
	def clear(self):
		self.markedTime = time()
		self.question.newQuestion()
		self.life.lifes = 3
		self.canPlay = True
		self.score = 0
