import arcade

from models import World, Question
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

scale = 0.6
Type = ["direction","color"]

Arrow = [[0 for x in range(4)] for y in range(4)]
question = [0,0]

class ThinkTwiceWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
 
		arcade.set_background_color(arcade.color.BLACK)
		
		self.world = World(width, height)

		self.image = [["images/green.png", "images/red.png", "images/blue.png", "images/yellow.png"],["images/left.png", "images/down.png", "images/up.png", "images/right.png"]]

		Arrow[2] = [230,370,370,510]
		Arrow[3] = [130,130,235,130]
		
		for i in range(0,2):
			question[i] = arcade.Sprite(self.image[i][self.world.question.questionRnd[i]],scale)
			question[i].set_position(530,390)
			for j in range(0,4):
				Arrow[i][j] = arcade.Sprite(self.image[i][j],scale)
				Arrow[i][j].set_position(Arrow[2][j],Arrow[3][j])

	def on_draw(self):
		arcade.start_render()
		 
		for i in range(0,2):
			question[i].draw()
			for j in range(0,4):
				Arrow[i][j].draw()
		
		arcade.draw_text("Which one has",250,460,arcade.color.WHITE, 20)
		arcade.draw_text("the same "+Type[self.world.question.rand_type]+" with",130,390,arcade.color.WHITE, 20)

	def on_key_press(self, key, modifiers):
		self.world.on_key_press(key, modifiers)

if __name__ == '__main__':
	window = ThinkTwiceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()
