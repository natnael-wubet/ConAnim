#import gravtest
import os
import time
import math
class P5py:
	width = 200
	height = 60
	screenData = []
	bg='_'
	stroke='.'
	fill='0'
	frameCount=0
	def ellipse(self,x,y,w,h):
		r = max(w,h)
		for i in range(0,r*10):
			tmpx1 = math.sin(i*10)*w
			tmpx2 = math.cos(i*10)*w
			tmpy1 = math.cos(i*10)*h
			tmpy2 = math.sin(i*10)*h
			self.point(x,y)
			self.point(x+tmpx1,y+tmpy1)
			#self.line(x+(tmpx1-w/2),y+(tmpy1-h/2),x+(tmpx2+w/2),y+(tmpy2+h/2))
	def line(self,x,y,x2,y2):
		xlen = abs(x2-x)
		ylen = abs(y2-y)
		total = math.sqrt(math.pow(xlen,2)+math.pow(ylen,2))
		for i in range(0,int(total)):

			xp = x + (i*(xlen/total)) * ( (x2<x)*-2 + 1)
			yp = y + (i*(ylen/total)) * ( (y2<y)*-2 + 1)
			self.point(xp,yp)
	def size(self,width,height):
		self.width = width
		self.height = height
		self.screenDate=[]
		self.initScreen(self.bg)
	def initScreen(self,bg):
		for j in range(0,self.height):
			self.screenData.append([self.bg]*self.width)
	def background(self,x):
		self.bg=x
		for j in range(0,self.height):
			self.screenData[j] =[self.bg]*self.width

	#initScreen(x)
	def __init__(self):
		self.initScreen(self.bg)
	def display(self):
		todisp = ''
		for j in range(0,self.height):
			for i in range(0,self.width):
				#print(i,j,self.height,self.width)
				todisp += str(self.screenData[j][i])
			todisp+='\n'
		print(todisp)


	def rect(self,x,y,w,h):
		l = 0
		for j in range(int(max(0,y)),int(min(y+h,self.height-1))):
			for i in range(int(max(0,x)),int(min(x+w,self.width-1))):
				l+=1
				#print(l,j,i)
				self.screenData[j][i] = self.fill
				#display()
	def circle(self,x,y,r):
		pass


	def point(self,x,y):
		x=int(x)
		y=int(y)
		if (x < self.width and x >=0) and (y <self.height and y>=0):
			self.screenData[y][x] = self.stroke
	
	def dsraw(self):
		self.background(' ')
		#rect(frameCount%width,1,10,5)
		for i in range(frameCount,frameCount+200):
			x = width/2+math.sin(i/40)*width/4
			y = height/2+math.cos(i/38)*height/4
			point(x,y,'o')
	'''
	while 1:
		display()
		time.sleep(.05)
		gravtest.draw()
		frameCount+=1
		os.system('clear')
    '''
class Runner:
    def __init__(self,script):
        self.p5 = P5py()
        self.app = script(self.p5)
    def run(self):
        while 1:
            time.sleep(.1)
            os.system("clear")
            self.p5.display()
            self.app.draw()
            self.p5.frameCount+=1
