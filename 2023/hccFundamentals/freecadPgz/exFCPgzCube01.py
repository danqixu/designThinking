# Exploration with PyGame Zero-animated tkinter windows.
# By Brygg Ullmer, Clemson University
# Begun 2023-10-05

import pygame as pg
import sys
import time
from   functools       import partial
from   pgzero.builtins import Actor, animate, keyboard
import pgzero

import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

#https://github.com/MariwanJ/COIN3D_Snippet/blob/main/02.1.HelloCone.py

cubeActor = {}

t1 = coin.SoTranslation()
t1.translation.setValue([5,5,5])


#pgzero.loaders.set_root('/home/bullmer/git/designThinking/2023/hccFundamentals/freecadPgz')

pgzero.loaders.set_root('c:/git/designThinking/2023/hccFundamentals/freecadPgz/')
a = Actor(pos=(0,0), image='single_pix')
cubeActor[0] = a

animation = animate(a, pos=(10,0), tween='accel_decel', duration=5)
lastTime  = time.time()

global cubeActor, t1, animation, lastTime

def updateCube():
  global cubeActor, t1, lastTime
  nt = time.time()
  dt = nt-lastTime
  lastTime = nt
  animation.update(dt)
  x, y = cubeActor[0].pos
  t1.translation.setValue([x, y, 0])

def update(): updateCube()

####### pygame zero update loop ####### 
#def update(): 
#  root.update() #keeps TkInter alive
#root.mainloop()

view = Gui.ActiveDocument.ActiveView
sg = view.getSceneGraph()

root = coin.SoSeparator()
sg.addChild(root)


c1 = coin.SoCube()
c2 = coin.SoCube()

C1 = coin.SoMaterial()
C1.diffuseColor.setValue([1,0,0])

for child in [c1, t1, C1, c2]: root.addChild(child)

DISPLAY_FLAGS = pygame.SHOWN
pygame.display.set_mode((100,100), flags=(DISPLAY_FLAGS & ~pygame.SHOWN) | pygame.HIDDEN,)
pygame.display.init()

#idlecallback to drive animation updates

### end ###
