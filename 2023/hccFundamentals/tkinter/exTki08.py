# Example code relating to interactive storyboarding
# By Brygg Ullmer, Clemson University
# Begun 2023-11-08

from tkinter import *
import PIL.Image, PIL.ImageTk #image manipulation package

#WIDTH=1024

screenStates = ['unsdg2', 'unsdg4']
imgAddUser   = 'person-add-iconic1'

#actorNames           = {a1: "John", a2: "Jane", s1: "screen", b1: "addUser"}
actorOriginalPos     = {}
selectedActor        = None
selectedActorName    = None
selectedActorOrigPos = None

def helloCB():
  print("hello was pushed")

#screen.draw.circle((800, 500), 50, defaultEllipseColor)
#
####################### on mouse down/press ######################
#
#def addUser():
#  newActor = Actor('red-hl-1in-200dpi',  pos=(200, 200))
#  moveableActors.append(newActor)
#  actorNames[newActor] = 'new actor'
#
####################### on mouse down/press ######################
#
#def on_mouse_down(pos):
#  global selectedActor, selectedActorName, selectedActorOrigPos, stableActors
#  for actor in (stableActors + moveableActors):
#    if actor.collidepoint(pos): 
#      name = actorNames[actor]
#      print("\nactor selected:", name)
#
#      if name == "screen": 
#        print("update the virtual screen images")
#        stableActors = [s2, b1]
#
#      elif name == "addUser":
#        addUser()
#
#      else:
#        actorOriginalPos[actor] = pos     
#        selectedActor           = actor
#        selectedActorName       = name
#        selectedActorOrigPos    = selectedActor.pos
#
#  print("=" * 25)
#
#def on_mouse_move()
#
####################### on mouse up ######################
#
#def on_mouse_up():
#  global selectedActor, selectedActorName, selectedActorOrigPos
#  selectedActor = selectedActorName = selectedActorOrigPos = None
#
####################### on key down ######################
#
#numTimesSpaceHit = 0
#
#def on_key_down(key):
#  global numTimesSpaceHit
#
#  if key == keys.SPACE:  # keys.RIGHT, keys.H, keys.C, etc.
#    print("space pressed")
#
#    #match numTimesSpaceHit:
#    #  case 0:
#
#    if numTimesSpaceHit == 0:
#      animate(a1, pos=(400, 500), tween='accel_decel', duration=.75)
#    else:
#      animate(a2, pos=(500, 500), tween='accel_decel', duration=.75)
#
#    numTimesSpaceHit += 1
#
####################### build UI ######################

imP1 = imTk1 = None
imP2 = imTk2 = None

#https://stackoverflow.com/questions/51591456/can-i-use-rgb-in-tkinter
#translates rgb values of type int to a tkinter friendly color code
def rgb2tk(r, g, b):
  return "#%02x%02x%02x" % (r,g,b)

####################### build user interface ######################

def buildUI(f1Screens, f2Spatial, f3Controls):
  global imP1, imTk1, imP2, imTk2

  imgAddUserFn   = 'person-add-iconic1.png'
  imP1  = PIL.Image.open(imgAddUserFn)
  imTk1 = PIL.ImageTk.PhotoImage(imP1)

  #b = Button(f3Controls, text="add actor", command=helloCB) # Create a label with words
  b  = Button(f3Controls, image=imTk1, command=helloCB)
  b.pack(side=LEFT, expand=True, fill=BOTH) 

  screenFilenames = ['unsdg2.png', 'unsdg4.png']
  imP2   = PIL.Image.open(screenFilenames[0])
  imTk2  = PIL.ImageTk.PhotoImage(imP2)
  label1 = Label(f1Screens, image=imTk2)
  label1.pack()

  bgColor = rgb2tk(10, 10, 10)
  #c = Canvas(f2Spatial, bg="orange", height=200, width=1024)
  c = Canvas(f2Spatial,  bg=bgColor,  height=400, width=1024)
  c.pack()

  r1Coords = (10, 10, 60, 60)
  c.create_rectangle(r1Coords, fill="white")

  r2Coords = (70, 10, 120, 60)
  c.create_rectangle(r2Coords, fill="orange")

####################### main ######################

root = Tk() # Create the root (base) window

f1Screens  = Frame(root)
f2Spatial  = Frame(root)
f3Controls = Frame(root)
buildUI(f1Screens, f2Spatial, f3Controls)

for frame in [f1Screens, f2Spatial, f3Controls]: 
  frame.pack(side=TOP, expand=True, fill=BOTH)

root.mainloop()                                            # Start the event loop

### end ###
