#Diego Aspinwall
#10-5-17
#dotsDemo.py - Making some dots

from ggame import *

red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)

dot = CircleAsset(20, LineStyle(1,red), red)
dot2 = CircleAsset(10, LineStyle(1,blue), red)

for j in range(10): #prints the row 10 times
    for i in range(20): #prints one row of dots
        Sprite(dot, (20+50*i,20+50*j))
for a in range(10):
    for b in range(20):
        Sprite(dot, (30+50*b,30+50*a))
App().run()
