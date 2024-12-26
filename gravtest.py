from main import P5py
import time
import os
def setup():
	pass
class Grav():
	global speed
	global acc
	global y
	yofp = 4
	xofp = 10
	sofp=.5
	def __init__(self):
		#self.yofp = p5.height
		self.speed=0
		self.acc=.005
		self.y=3
	def draw(self):
		p5.background(' ')
		p5.fill = '_'
		print(self.speed,int(p5.height-self.y),self.acc)
		p5.rect(1,int(p5.height-self.y),p5.width-20,p5.height)
		p5.fill = '|'
		p5.rect(25,int(p5.height-self.y-6),10,6)

		p5.fill = '*'

		p5.rect(self.xofp,p5.height-self.yofp-1,3,2)
		self.speed+=self.acc
		self.y+=self.speed
		self.speed+=self.acc
		#if (self.yofp <= self.y):
		#	self.yofp=self.y
		#self.yofp += .3
		self.xofp += ((self.yofp <= self.y)*0) + ((self.yofp > self.y)*self.sofp)


		self.yofp = ((self.yofp <= self.y)*self.y) + ((self.yofp >self.y)*(self.yofp+self.sofp))


		if self.y >p5.height*2:
			self.speed=0
			self.y=2
			self.xofp=10
			self.yofp=3
			#p5.height

p5 = P5py()
app=Grav()
while 1:
	time.sleep(.1)
	os.system('clear')
	p5.display()
	#time.sleep(.5)
	#app.setup()
	app.draw()
	p5.frameCount+=1
	

