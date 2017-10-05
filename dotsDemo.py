#Diego Aspinwall
#10-5-17
#dotsDemo.py - Making some dots

from ggame import *

red = Color(0xFF0000,1)

dot = CircleAsset(20, LineStyle(1,red), red)

Sprite(dot, (20,20))
App().run()
