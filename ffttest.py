import math
from main import Runner

class Script():
	def __init__(self,p5):
		self.p5 = p5
		self.p5.size(300,70)
		self.p5.background(" ")		
		self.fft = self.FFt(p5);
		self.p5.stroke="🧑"		
		self.p5.fill = self.p5.stroke
	class FFt():
        
		def __init__(self,p5):
			self.dataA = []
			self.dataB = []
			self.dataC = []
			self.dataCombine = []
			for i in range(0,p5.width):
				self.dataB.append(i)
				self.dataA.append(i)
				self.dataC.append(i)
				self.dataCombine.append(i)
			pass
		def drawA(self,p5):
			for i in range(0,p5.width):
				self.dataA[i] = math.sin((i+(p5.frameCount*3))/6)*(p5.height/15)
				p5.point(i,p5.height/15+self.dataA[i])
		def drawB(self,p5):
			for i in range(0,p5.width):
				self.dataB[i] = math.cos((i+p5.frameCount)/7)*(p5.height/15)
				p5.point(i,((p5.height/15)*3)+self.dataB[i])
		def drawC(self,p5):
                        for i in range(0,p5.width):
                                self.dataC[i] = math.sin((i+(4*p5.frameCount))/5)*(p5.height/15)
                                p5.point(i,((p5.height/15)*6)+self.dataC[i])

		def drawCombine(self,p5):
                        for i in range(0,p5.width):
                                self.dataCombine[i] = (self.dataA[i]+self.dataB[i]+self.dataC[i])/2 #math.sin((i+p5.frameCount)/10)*(p5.height/10)
                                p5.point(i,((p5.height/10)*9)+self.dataCombine[i])


	def draw(self):
		
		self.p5.background(' ')
		height = self.p5.height
		width = self.p5.width
		self.fft.drawA(self.p5)
		self.fft.drawB(self.p5)
		self.fft.drawC(self.p5)
		self.fft.drawCombine(self.p5)


runner = Runner(Script)
runner.run()
