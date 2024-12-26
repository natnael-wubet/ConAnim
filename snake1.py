import math
import random

class Script():
    def __init__(self,p5):
        self.p5 = p5
        self.p5.size(400,50)
        self.p5.background(" ")
        self.counts = 6
        self.p5.stroke="*"
        self.circles = [[0,0]]
        for i in range(0,self.counts-1):
            self.circles+=[[0,0]]
        self.locations = [range(0,self.p5.width),range(0,self.p5.height)]
        self.randFood()
    def randFood(self):
        self.food = [random.choice(self.locations[0]),random.choice(self.locations[1])]
    def draw(self):
        self.p5.background(' ')
        self.p5.point(self.food[0],self.food[1])
        diff=0
               
        width = self.p5.width
        height = self.p5.height

        for i in range(0,self.counts):
            radius = int((self.counts-i)*1)

            tmpx=0
            tmpy=0
            #self.p5.ellipse(self.circles[i][0],self.circles[i][1],radius,radius)
            if (i==0):
                tmpx = (self.food[0]-self.circles[i][0])/(width/6)
                tmpy = (self.food[1]-self.circles[i][1])/(height/6)
            else:
                tmpx = (self.circles[i-1][0]-self.circles[i][0])/(width/6)
                tmpy = (self.circles[i-1][1]-self.circles[i][1])/(height/6)
               
            if (i==0):
                diff += abs(tmpx) + abs(tmpy)
            self.circles[i][0] += tmpx
            #print(i,self.circles[i][0],tmpx,tmpy,'""""',self.circles[i-1][0],self.circles[i][0])
            #self.p5.line(self.circles[i][0],self.circles[i][1],self.circles[i-1][0],self.circles[i-1][1])
                
            self.circles[i][1] += tmpy
        for i in range(0,self.counts):
            if (i>0):
                self.p5.line(self.circles[i][0],self.circles[i][1],self.circles[i-1][0],self.circles[i-1][1])
                #print( self.circles[i][0],self.circles[i][1],self.circles[i-1][0],self.circles[i-1][1])
           
        if (diff<=1):
            self.randFood()
