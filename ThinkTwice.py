import arcade
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

scale = 0.6

RED = (255, 0, 0)
 
class ThinkTwiceWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
 
		arcade.set_background_color(arcade.color.BLACK)
		
		self.leftArrow = arcade.Sprite('images/left.png',scale)
		self.leftArrow.set_position(230,150)		
		self.green = arcade.Sprite('images/green.png',scale)
		self.green.set_position(230,150)

 		
		self.downArrow = arcade.Sprite('images/down.png',scale)
		self.downArrow.set_position(370,150)		
		self.red = arcade.Sprite('images/red.png',scale)
		self.red.set_position(370,150)
		
		self.upArrow = arcade.Sprite('images/up.png',scale)
		self.upArrow.set_position(370,255)		
		self.blue = arcade.Sprite('images/blue.png',scale)
		self.blue.set_position(370,255)
	
		self.rightArrow = arcade.Sprite('images/right.png',scale)
		self.rightArrow.set_position(510,150)		
		self.yellow = arcade.Sprite('images/yellow.png',scale)
		self.yellow.set_position(510,150)

	def on_draw(self):
		arcade.start_render()
		 
		self.green.draw()
		self.leftArrow.draw()
		
		self.blue.draw()
		self.upArrow.draw()

		self.red.draw()
		self.downArrow.draw()

		self.yellow.draw()
		self.rightArrow.draw()

if __name__ == '__main__':
	window = ThinkTwiceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()
