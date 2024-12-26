import math
class Script():
	def __init__(self,p5):
		self.p5 = p5
		self.p5.size(200,30)
		self.p5.background("'")
		self.p5.stroke = '*'
		self.charset = "☄️.~!@#$%^&*()_+=-{}[]:./,./,';`\\|OliozZ0123456789qwertyuiplkjhgfdsdfxzcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
		pass
	def draw(self):
		self.p5.background(' ')
		height = self.p5.height
		width = self.p5.width
		for i in range(0,10+int(self.p5.frameCount/50)):
			self.p5.stroke = self.charset[i%len(self.charset)]
			f = self.p5.frameCount+(i*3)		
			x = width/2+math.sin(f/32)*width/3
			y = height/2+math.cos(f/32)*height/3
			x2 = width/2+math.sin(f/36)*width/3
			y2 = height/2+math.cos(f/36)*height/3
			self.p5.line(x,y,x2,y2)
			self.p5.stroke = '*'
		#self.p5.point(i/10,y2)
		#self.p5.stroke = 'o'
			
		#self.p5.rect(1,1,10,10)
