import arcade

#from models import Arrow
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

scale = 0.6

Arrow = [[0 for x in range(4)] for y in range(4)]
    
class ThinkTwiceWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
 
		arcade.set_background_color(arcade.color.BLACK)
		
		self.leftArrow = arcade.Sprite('images/left.png',scale)
		self.green = arcade.Sprite('images/green.png',scale)

		self.downArrow = arcade.Sprite('images/down.png',scale)
		self.red = arcade.Sprite('images/red.png',scale)
		
		self.upArrow = arcade.Sprite('images/up.png',scale)
		self.blue = arcade.Sprite('images/blue.png',scale)
	
		self.rightArrow = arcade.Sprite('images/right.png',scale)
		self.yellow = arcade.Sprite('images/yellow.png',scale)

		Arrow[0] = [self.green, self.red, self.blue, self.yellow]
		Arrow[1] = [self.leftArrow, self.upArrow, self.downArrow, self.rightArrow]
		Arrow[2] = [230,370,370,510]
		Arrow[3] = [150,150,255,150]

		for i in range(0,4):
			Arrow[0][i].set_position(Arrow[2][i],Arrow[3][i])
			Arrow[1][i].set_position(Arrow[2][i],Arrow[3][i])

	def on_draw(self):
		arcade.start_render()
		 
		for i in range(0,2):
			for j in range(0,4):
				Arrow[i][j].draw()

if __name__ == '__main__':
	window = ThinkTwiceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()
