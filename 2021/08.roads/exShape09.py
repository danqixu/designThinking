# Enodia Shapefile abstractions
# Brygg Ullmer, Clemson University
# Begun 10/02/2021

#https://www.visualcapitalist.com/wp-content/uploads/2017/10/interstate-highways-map.html

from enShapefile import *

import csv, traceback
capitolsFn = 'state-capitols.csv'
capitolsF  = open(capitolsFn, 'r+t')
dataReader = csv.reader(capitolsF, delimiter=',');

es       = enShapefile()
es.targetRoads = []

for i in range(10, 91, 10): es.targetRoads.append(i)
for i in range( 5, 96, 10): es.targetRoads.append(i)

manualList = [82,84,86,94, 17,29,24,43,77,79,81,87, 26]

for road in manualList: es.targetRoads.append(road)

print('targetRoads:', es.targetRoads)

#es.targetRoads = [10, 90,  5, 95]

es.extractInterstateVerts()
es.calcLatLongMinMaxRange()

rvs      = es.roadVertexSeqs
rvsNames = rvs.keys()

es.plotCaiCreateSurface()

for rvsName in rvsNames:      #primary road names
  for rvSeq in rvs[rvsName]: #list of constituitive vertex sequences
    es.plotCaiVertSeq(rvSeq)

#es.drawCircle([-81, 34], .02) #, Columbia, SC

firstline = True; lineNum = 0

for capitolDS in dataReader: #state capitol data structure
  if firstline: firstline = False; continue
  city, state, long, lat = capitolDS; lineNum += 1
  #if lineNum == 31: es.drawCircle([float(lat), float(long)], .02) 

  try:    es.drawCircle([float(lat), float(long)], .02) 
  except: print(traceback.print_exc())

es.ctx.stroke()

es.plotCaiWritePng("ex09.png")
    
### end ###
