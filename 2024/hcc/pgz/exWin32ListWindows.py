#https://stackoverflow.com/questions/14653168/get-hwnd-of-each-window

import win32gui

def enumHandler(hwnd, lParam):
  winText = win32gui.GetWindowText(hwnd)
  if win32gui.IsWindowVisible(hwnd) and len(winText) > 0: print(winText)

#    if 'Stack Overflow' in win32gui.GetWindowText(hwnd):
#       win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)

win32gui.EnumWindows(enumHandler, None)

### end ###