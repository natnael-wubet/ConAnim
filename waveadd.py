import math
class Script():
	def __init__(self,p5):
		self.p5 = p5
		self.p5.size(400,70)
		self.p5.background("'")
		self.p5.stroke = '*'
		pass
	def draw(self):
		self.p5.background(' ')
		height = self.p5.height
		width = self.p5.width
		for i in range(0,self.p5.width*20):
			y = (height/2)+(math.sin((i+35*self.p5.frameCount)/50)*(height/2.5))
			y2 = (height/2)+(math.cos((i+35*self.p5.frameCount)/62)*(height/2.5))
			self.p5.point(i/10,y)
			self.p5.stroke = '☄️'
		
			self.p5.point(i/10,(y+y2)/2)
			self.p5.stroke = '.'
			self.p5.point(i/10,y2)
			self.p5.stroke = '"'
			
		#self.p5.rect(1,1,10,10)
