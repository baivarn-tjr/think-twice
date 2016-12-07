import arcade

from models import World, Question
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

scale = 0.6
Type = ["color","direction"]

Arrow = [[0 for x in range(4)] for y in range(4)]
question = [0,0]

class ThinkTwiceWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
 
		arcade.set_background_color(arcade.color.BLACK)
		
		self.world = World(width, height)
		self.heart = []

		self.image = [["images/green.png", "images/red.png", "images/blue.png", "images/yellow.png"],["images/left.png", "images/down.png", "images/up.png", "images/right.png"]]

		Arrow[2] = [230,370,370,510]
		Arrow[3] = [130,130,235,130]

		for i in range(0,3):
			self.heart.append(arcade.Sprite("images/heart.png",0.8))
			self.heart[i].set_position(40+(i*50), 550)
					
		for i in range(0,2):
			question[i] = arcade.Sprite(self.image[i][self.world.question.questionRnd[i]],scale)
			question[i].set_position(530,390)
			for j in range(0,4):
				Arrow[i][j] = arcade.Sprite(self.image[i][j],scale)
				Arrow[i][j].set_position(Arrow[2][j],Arrow[3][j])

	def on_draw(self):
		arcade.start_render()
		if(self.world.canPlay): 
			for i in range(0,2):
				question[i].draw()
				for j in range(0,4):
					Arrow[i][j].draw()
		
			for i in range(0,self.world.life.lifes):
				self.heart[i].draw()

			arcade.draw_text("Which one has",250,460,arcade.color.WHITE, 20)
			arcade.draw_text("the same "+Type[self.world.question.rand_type]+" with",130,390,arcade.color.WHITE, 20)
			arcade.draw_text("score: "+ str(self.world.score),650,550, arcade.color.WHITE, 18)
			arcade.draw_text("time: "+str(int(4-self.world.time)),350,550,arcade.color.WHITE, 18)

		else:
			arcade.draw_text("your score is  "+ str(self.world.score),300,400,arcade.color.WHITE, 22)
			
	def animate(self, delta):
		self.update_question()
		self.world.animate(delta)

	def update_question(self):	
		for i in range(0,2):
			question[i] = arcade.Sprite(self.image[i][self.world.question.questionRnd[i]],scale)
			question[i].set_position(530,390)

	def on_key_press(self, key, modifiers):
		self.world.on_key_press(key, modifiers)

if __name__ == '__main__':
	window = ThinkTwiceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()
