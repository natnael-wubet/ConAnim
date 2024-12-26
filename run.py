import os
import sys
lab = '''
from main import P5py
import time
import os
from %s import Script
p5 = P5py()
app = Script(p5)
while 1:
	time.sleep(.1)
	os.system("clear")
	p5.display()
	app.draw()
	p5.frameCount+=1
    '''%(sys.argv[1])
os.system("echo '%s' >tmp.py"%lab)
os.system("python3 tmp.py")
