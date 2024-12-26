import math
from time import sleep
import random
class Script():
	def __init__(self,p5):
		self.p5 = p5
		self.p5.size(300,70)
		self.p5.background("'")
		self.p5.stroke = '*'
		self.charset = "~!@#$%^&*()_+=-{}[]:./,./,';`\\|OliozZ0123456789qwertyuiplkjhgfdsdfxzcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
		self.x = 0
		self.y = 0
		self.dx = 1
		self.dy = 1
		self.spacing = min(self.p5.width,self.p5.height)
		self.spx = 10

		self.playerA = self.Ping(0,random.choice(range(0,self.p5.height-10)))
		sleep(random.choice(range(1,6)))
		self.playerB = self.Ping(self.p5.width-(1+self.playerA.width),random.choice(range(0,self.p5.height-10)))
		self.pong = self.Pong(p5)
	class Pong():
		def __init__(self,p5):
			self.reset(p5)
		def reset(self,p5):
			self.x = p5.width/2
			self.y = p5.height/2
			self.rad = 3
			possibleD = []
			for i in range(-50,50):
				possibleD.append(i/10)
			self.dx = random.choice(possibleD)
			self.dy = random.choice(possibleD)
			return 1
		def draw(self,p5,playerA,playerB):
			p5.ellipse(self.x,self.y,self.rad,self.rad)
			self.x += self.dx
			self.y += self.dy
			if (self.x+self.rad>p5.width-(playerB.width)):
				if (self.y+self.rad > playerB.posy) & (self.y-self.rad < playerB.posy+playerB.height):
					self.dx =self.dx*-1
				else:
					self.reset(p5)
			if (self.x-self.rad<playerA.width):
				if (self.y+self.rad > playerA.posy) & (self.y-self.rad < playerA.posy+playerA.height):
					self.dx =self.dx*-1
				else:
					self.reset(p5)
                         

			self.dy = self.dy * (1+(-2*((self.y+self.rad>p5.height)|(self.y-self.rad<0))))
	class Ping():
		def __init__(self,posx,posy):
			self.posx = posx
			self.posy = posy
			self.width = 2
			self.height = 10
			self.dy = random.choice([-1,1])
		def draw(self,p5):
			p5.fill = '#'
			p5.rect(self.posx,self.posy,self.width,self.height)
			self.dy = self.dy * (1+ (-2*((self.posy<0)|((self.posy+self.height)>p5.height))))
			self.posy+=self.dy
	def draw(self):
		self.p5.background(' ')
		self.playerB.draw(self.p5)
		self.playerA.draw(self.p5)
		self.pong.draw(self.p5,self.playerA,self.playerB)
		#self.p5.rect(1,1,10,10)
