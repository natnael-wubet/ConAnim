
import math
class Script():
    def __init__(self,p5):
        self.p5 = p5
        self.p5.size(100,30)
        self.p5.background("'")
        self.p5.stroke = '*'
        pass

    def tree(self,x,r,height):

        if (x<=0): return 0;
        h =10-x 
        width = self.p5.width
        sin = math.sin
        line=self.p5.line
        line(width/2,height,width/2,height-(h-x))
        line(width/2,height-(h-x),width/2 -(r+sin(x)),height-((h*1.5)-x))
        line(width/2,height-(h-x),width/2 +(r+sin(x)),height-((h*1.5)-x))
        self.tree(x-1,r,height-((h*1.5)-x))
        
    def draw(self):
        self.p5.background(' ')
        height = self.p5.height
        width = self.p5.width	
        self.tree(3,3,height)
        #self.p5.rect(1,1,10,10)
