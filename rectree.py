class Script():
	def __init__(self,p5):
		self.p5 = p5
		self.p5.size(100,30)
		self.p5.background(' ')
		self.p5.stroke = '*'
	def frac(self,i):

		pass
	def draw(self):
		self.p5.background(' ')
		height = self.p5.height
		point = self.p5.point
		point(2,2)
		point(10,2)
		point(2,20)
		point(10,20)
		self.p5.line(2,2,10,20)
