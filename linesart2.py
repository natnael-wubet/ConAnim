import math


class Script():
    def __init__(self, p5):
        self.p5 = p5
        self.p5.size(200, 100)
        self.p5.background("'")
        self.p5.stroke = '*'
        self.charset = "☄️.~!@#$%^&*()_+=-{}[]:./,./,';`\\|OliozZ0123456789qwertyuiplkjhgfdsdfxzcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    def draw(self):
        self.p5.background(' ')
        height = self.p5.height
        width = self.p5.width
        p5 = self.p5
        sin = math.sin
        cos = math.cos
        f = p5.frameCount*20

        for i in range(0, 100):
            p5.stroke=self.charset[i+1]
            
            x = width / 2 + sin(((7.5*i+f)) / 99) * width / 2

            y = height / 2 + cos((6*i + f) / 100) * height / 2

            x2 = width / 2 + sin(((5.5*i+f)) / 90) * width / 2

            y2 = height / 2 + cos((4*i + f) / 91) * height / 2

            p5.line(x,y,x2,y2)

        # Uncomment the following lines if you want to use them
        # for i in range(0, 50 + int(self.p5.frameCount / 50)):
        #     self.p5.stroke = self.charset[i % len(self.charset)]
        #     f = self.p5.frameCount + (i * 3)
        #     x = width / 2 + math.sin(f / 32) * width / 3
        #     y = height / 2 + math.cos(f / 32) * height / 3
        #     x2 = width / 2 + math.sin(f / 36) * width / 3
        #     y2 = height / 2 + math.cos(f / 36) * height / 3
        #     self
