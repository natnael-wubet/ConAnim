import math
class Script():
	def __init__(self,p5):
		self.p5 = p5
		self.p5.size(110,40)
		self.p5.background("'")
		self.p5.stroke = '*'
		self.charset = "~!@#$%^&*()_+=-{}[]:./,./,';`\\|OliozZ0123456789qwertyuiplkjhgfdsdfxzcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
		self.x = 0
		self.y = 0
		self.dx = 1
		self.dy = 1
		self.spacing = min(self.p5.width,self.p5.height)
		self.spx = 10
		pass
		
	def draw(self):
		self.p5.background(' ')
		height = self.p5.height
		width = self.p5.width
		s = self.spacing
		self.spacing -= ((self.x == 0) + (self.x == width) + (self.y==height) + (self.y==0))*self.spx
		if self.spacing <=0:
			self.spacing = abs(self.spx)
			self.spx = self.spx*-1
		elif self.spacing > min(width,height):
			self.spacing = min(width,height)
			self.spx = self.spx*-1
		for i in range(0,int(height/s)):
			self.p5.stroke = '+'
			self.p5.line(0,i*s,self.x,self.y)
			self.p5.stroke = '.'
			self.p5.line(width,i*s,self.x,self.y)
		for i in range(0,int(width/s)):
			self.p5.stroke = ';'
			self.p5.line(i*s,0,self.x,self.y)
			self.p5.stroke = 'o'
			self.p5.line(i*s,height,self.x,self.y)
		self.dx = self.dx * ( ((self.x>=width) | (self.x<0))*-2 + 1)
		self.dy = self.dy * ( ((self.y>=height) | (self.y<0))*-2 +1)
		self.x+=self.dx
		self.y+=self.dy
		print(self.y>=height, self.y<=0 , ((self.y>=height) | (self.y<=0)))
		print(self.x,self.y,self.dx,self.dy,width,height)
		
			
		#self.p5.rect(1,1,10,10)
