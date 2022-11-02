# Brygg Ullmer, Clemson University
# Begun 2022-11-01
# Content engaging https://github.com/DataKind-DC/homelessness-service-navigator

from PIL import Image, ImagePgz
from enoDomHomelessness import *

class enoUiHomelessnessPgz:

  edh          = None  #enoDomHomelessness
  tkParent     = None  #tk parent
  tkFrame      = None
  tkButtons    = None 

  imageHandles = None

  ####################### constructor #######################

  def __init__(self, tkParent):
    self.edh = enoDomHomelessness()
    self.buildUI(tkParent)

  ####################### build UI #######################

  def buildUI(self, tkParent):
    self.tkParent  = tkParent 
    self.tkFrame   = tk.Frame(tkParent, bg="#44AB9D")
    self.tkButtons = {}; self.imageHandles = {}
    
    categories = self.edh.getCategories()
    for category in categories:
      imgFn1 = self.edh.getImageFn(category)
      imgFn2 = "images/%s.png" % imgFn1
      img    = ImagePgz.PhotoImage(file=imgFn2)
      self.imageHandles[category] = img #amazing; this line necessary, per atlasologist reference here
      # https://stackoverflow.com/questions/22200003/tkinter-button-not-showing-image

      b = tk.Button(self.tkFrame, image=img, bg="#44AB9D", borderwidth=0) #no button border
      #b.pack(expand=True, fill="x", anchor="w") #this centers the images, which isn't my preference
      b.pack(expand=True, anchor="w")
    self.tkFrame.pack()

  ####################### draw #######################

  def buildUI(self, tkParent):

  ####################### draw #######################

  def onMouseDown(self, pos):

####################### main #######################
if __name__ == '__main__':
  top = tk.Pgz()
  enoUiH = enoUiHomelessnessPgz(top)
  top.mainloop()

### end ###
