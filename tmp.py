
from main import P5py
import time
import os
from ffttest import Script
p5 = P5py()
app = Script(p5)
while 1:
	time.sleep(.1)
	os.system("clear")
	p5.display()
	app.draw()
	p5.frameCount+=1
    
