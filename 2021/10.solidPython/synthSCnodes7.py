# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-27

from solid import *        # load in SolidPython/SCAD support code
import csv
from mcmBolts import *

scPopCoordFn = 'sc-pop-coord.csv'; scPCF = open(scPopCoordFn, "r")
scpcReader   = csv.reader(scPCF, delimiter=",")

hlCities = ['Clemson', 'Greenville', 'Columbia', 'Charleston', 'Hartsville', 'Travelers Rest'] #highlight cities

#minMaxLatLong = [32.1632, 35.156486, -78.67792, -83.110782]
#minMaxLatLong = [32.0632, 35.256486, -78.77792, -83.010782]
#minMaxLatLong = [31.5, 35.8, -79, -84]
#minMaxLatLong = [31.5, 35.5, -79., -84.]
minMaxLatLong = [31.9, 35.5, -78.5, -83.5]

############### buildGroundPlane ###############

def buildGroundPlane(multiplier):
  global minMaxLatLong 
  minlat, maxlat, minlong, maxlong = minMaxLatLong 

  difflat  = abs(maxlat - minlat)
  difflong = abs(maxlong - minlong)

  difflat2  = difflat  * multiplier
  difflong2 = difflong * multiplier

  cx = (minlong + maxlong)/2 * multiplier 
  cy = (minlat + maxlat)/2 * multiplier 

  print(difflat2, difflong2, cx - difflat2/2, cy)

  c1 = cube([difflat2, difflong2, 7])
  c2 = translate([cy-difflong2/2.5, cx-difflat2/1.5, 0])(c1)
  c3 = color([.5,.5,.6])(c2)
  return c3

############### map pop 2 bolt ###############

#boltPopHash  = boltPopHashY = {0: 'n0', 30000: 'n0', 75000: 'n4', 200000: 'n1_4'}
boltPopHash  = boltPopHashY = {0: 'n0', 20000: 'n0', 30000: 'n2', 75000: 'n4', 200000: 'n1_4'}

def mapPop2Bolt(popStr, boltObj, boltPopHash):
  global   boltSpec
  try:     pop = int(popStr)
  except:  return 1

  popThresh = boltPopHash.keys()
  idx = 0
  for testPop in popThresh:
    if pop > testPop: idx += 1
    else:             
      key = list(popThresh)[idx]
      boltSpec = boltPopHash[key]
      #print("bs1:", boltSpec)
      return boltObj.synthBoltNeutral(boltSpec)
  lpt = len(popThresh)
  if idx >=lpt: idx = lpt-1
  try:
    key = list(popThresh)[idx]
    boltSpec = boltPopHash[key]
    #print("bs2:", boltSpec)
    return boltObj.synthBoltNeutral(boltSpec)
  except: return -1

############### main ###############

multiplier = 65.

boltObj = mcmBolts()
outGeom = buildGroundPlane(multiplier)

minlat, maxlat, minlong, maxlong = [None, None, None, None]

for row in scpcReader:
  city, popStr, lat, long = row
  bolt1 = mapPop2Bolt(popStr, boltObj, boltPopHash)

  #if city=="Columbia": print(city, bolt1)
  if isinstance(bolt1, int): continue #ignore errors


  if boltSpec == 'n0': bolt2 = translate([0,0,3])(rotate([0,-90,0])(bolt1))
  else:                bolt2 = rotate([180,0,0])(bolt1)

  #if minlat == None or lat < minlat: minlat = lat
  #if maxlat == None or lat > maxlat: maxlat = lat

  #if minlong == None or long < minlong: minlong = long
  #if maxlong == None or long > maxlong: maxlong = long

  coord = [float(lat)*multiplier, float(long)*multiplier, 0]
  #print("coord:", coord, str(bolt))
  y2 = translate(coord)(bolt2)
  #print(city, y2)

  if outGeom == None:    outGeom = y2
  elif city in hlCities: outGeom += color([1,.5,0])(y2)
  else:                  outGeom += y2

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export

#print(minlat, maxlat, minlong, maxlong)

scad_render_to_file(outGeom, 'scNodes7.scad', file_header=hdr) # write the .scad file

### end ###

