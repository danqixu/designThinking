# Make partial extraction of CSV-save of tribe_entity_mapping sheet from this source:
#  https://www.epa.gov/sites/production/files/2021-03/tribe_entity_mapping_2021-03-04.xlsx
#  into YAML.
# (Exploratory version to facilitate related conversations.)
# Brygg Ullmer, Clemson University
# Begun 2023-11-21

import csv

csvFn = 'tribe_entity_mapping_2021-03-04.csv'
targetColumns = []

csvF  = open(csvFn, 'rt')
csvR  = csv.reader(csvF, delimter=',', quotechar='"')

for row in csvR:
  print("TBD")

### end ###