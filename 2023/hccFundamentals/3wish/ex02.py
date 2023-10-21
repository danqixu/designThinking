# First validation of Python port of 1995 3wish code
# Brygg Ullmer, Clemson University
# Original code begun fall 1995; here, 2023-10-20

import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin
import sys

sys.path.append('c:/git/designThinking/2023/hccFundamentals/3wish')
from w3core import *

##################### main #####################

if Gui.ActiveDocument is None:
  doc  = App.newDocument()
  doc.recompute()
  viewer = Gui.createViewer()
  view   = viewer.getViewer()
else:
  view = Gui.ActiveDocument.ActiveView

sg      = view.getSceneGraph()
root    = coin.SoSeparator()
sg.addChild(root)

cub1 = coin.SoCube()
addObj(root, cub1)

#view.redraw()
Gui.runCommand('Std_ViewZoomOut',0)
Gui.SendMsgToActiveView("ViewFit")

### end ###
