import arcade

#from models import Arrow
from random import randint
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

scale = 0.6

Arrow = [[0 for x in range(4)] for y in range(4)]

Type = ["direction","color"]
rand_type = randint(0,1)
rand_direction = randint(0,3)
rand_color = randint(0,3)

question = [rand_color,rand_direction]

class ThinkTwiceWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
 
		arcade.set_background_color(arcade.color.BLACK)
		
		self.image = [["images/green.png", "images/red.png", "images/blue.png", "images/yellow.png"],["images/left.png", "images/down.png", "images/up.png", "images/right.png"]]

		for i in range(0,2):
			for j in range(0,4):
				Arrow[i][j] = arcade.Sprite(self.image[i][j],scale)
				
		Arrow[2] = [230,370,370,510]
		Arrow[3] = [130,130,235,130]

		for i in range(0,4):
			Arrow[0][i].set_position(Arrow[2][i],Arrow[3][i])
			Arrow[1][i].set_position(Arrow[2][i],Arrow[3][i])

		self.questionColor = arcade.Sprite(self.image[0][question[0]],scale)
		self.questionDirection = arcade.Sprite(self.image[1][question[1]],scale)
		self.questionColor.set_position(530,390)
		self.questionDirection.set_position(530,390)

	def on_draw(self):
		arcade.start_render()
		 
		for i in range(0,2):
			for j in range(0,4):
				Arrow[i][j].draw()
		
		arcade.draw_text("Which one has",250,460,arcade.color.WHITE, 20)
		arcade.draw_text("the same "+Type[rand_type]+" with",130,390,arcade.color.WHITE, 20)
		self.questionColor.draw()
		self.questionDirection.draw()

if __name__ == '__main__':
	window = ThinkTwiceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()
