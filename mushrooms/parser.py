"""
Expands the single letter codes in the raw agaricus-lepiota.csv into their meaningful codes.

Author: Michael VanDaniker
Date: 2015-11-19
"""

import csv

columns_codes = {
  "class": {
    "edible": "e", "poisonous": "p"
  },
  "cap-shape": {
    "bell":"b", "conical":"c", "convex":"x", "flat":"f", "knobbed":"k", "sunken":"s"
  },
  "cap-surface": {
    "fibrous":"f","grooves":"g","scaly":"y","smooth":"s"
  },
  "cap-color": {
    "brown":"n","buff":"b","cinnamon":"c","gray":"g","green":"r","pink":"p","purple":"u","red":"e","white":"w","yellow":"y"
  },
  "bruises": {
    "true":"t","false":"f"
  },
  "odor": {
    "almond":"a","anise":"l","creosote":"c","fishy":"y","foul":"f","musty":"m","none":"n","pungent":"p","spicy":"s"
  },
  "gill-attachment": {
    "attached":"a","descending":"d","free":"f","notched":"n"
  },
  "gill-spacing": {
    "close":"c","crowded":"w","distant":"d"
  },
  "gill-size": {
    "broad":"b","narrow":"n"
  },
  "gill-color": {
    "black":"k","brown":"n","buff":"b","chocolate":"h","gray":"g", "green":"r","orange":"o","pink":"p","purple":"u","red":"e", "white":"w","yellow":"y"
  },
  "stalk-shape": {
    "enlarging":"e","tapering":"t"
  },
  "stalk-root": {
    "bulbous":"b","club":"c","cup":"u","equal":"e","rhizomorphs":"z","rooted":"r","missing":"?"
  },
  "stalk-surface-above-ring": {
    "fibrous":"f","scaly":"y","silky":"k","smooth":"s"
  },
  "stalk-surface-below-ring": {
    "fibrous":"f","scaly":"y","silky":"k","smooth":"s"
  },
  "stalk-color-above-ring": {
    "brown":"n","buff":"b","cinnamon":"c","gray":"g","orange":"o","pink":"p","red":"e","white":"w","yellow":"y"
  },
  "stalk-color-below-ring": {
    "brown":"n","buff":"b","cinnamon":"c","gray":"g","orange":"o","pink":"p","red":"e","white":"w","yellow":"y"
  },
  "veil-type": {
    "partial":"p","universal":"u"
  },
  "veil-color": {
    "brown":"n","orange":"o","white":"w","yellow":"y"
  },
  "ring-number": {
    "none":"n","one":"o","two":"t"
  },
  "ring-type": {
    "cobwebby":"c","evanescent":"e","flaring":"f","large":"l","none":"n","pendant":"p","sheathing":"s","zone":"z"
  },
  "spore-print-color": {
    "black":"k","brown":"n","buff":"b","chocolate":"h","green":"r","orange":"o","purple":"u","white":"w","yellow":"y"
  },
  "population": {
    "abundant":"a","clustered":"c","numerous":"n","scattered":"s","several":"v","solitary":"y"
  },
  "habitat": {
    "grasses":"g","leaves":"l","meadows":"m","paths":"p","urban":"u","waste":"w","woods":"d"
  }
}

"""
The columns_codes above are taken from http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names
which maps descriptions to codes, so the first step is to reverse that dictionary so we have a mapping of keys to descriptions.
"""
column_code_lookup = {}
for k, v in columns_codes.iteritems():
  column_code_lookup[k] = {}
  for k1, v1 in v.iteritems():
    column_code_lookup[k][v1] = k1

output_rows = []
with(open('agaricus-lepiota.csv', 'rb')) as f:
  reader = csv.DictReader(f)
  for row in reader:
    output_row = {}
    for k, v in row.iteritems():
      output_row[k] = column_code_lookup[k][v]
    output_rows.append(output_row)

with(open('out.csv','wb')) as f:
  writer = csv.DictWriter(f, fieldnames=column_code_lookup.keys())
  writer.writeheader()
  for row in output_rows:
    writer.writerow(row)
    

"""
     1."cap-shape:"                bell":"b","conical":"c","convex":"x","flat":"f","
                                  knobbed":"k","sunken":"s
     2."cap-surface:"              fibrous":"f","grooves":"g","scaly":"y","smooth":"s
     3."cap-color:"                brown":"n","buff":"b","cinnamon":"c","gray":"g","green":"r","
                                  pink":"p","purple":"u","red":"e","white":"w","yellow":"y
     4."bruises?:"                 bruises":"t","no":"f
     5."odor:"                     almond":"a","anise":"l","creosote":"c","fishy":"y","foul":"f","
                                  musty":"m","none":"n","pungent":"p","spicy":"s
     6."gill-attachment:"          attached":"a","descending":"d","free":"f","notched":"n
     7."gill-spacing:"             close":"c","crowded":"w","distant":"d
     8."gill-size:"                broad":"b","narrow":"n
     9."gill-color:"               black":"k","brown":"n","buff":"b","chocolate":"h","gray":"g","
                                  green":"r","orange":"o","pink":"p","purple":"u","red":"e","
                                  white":"w","yellow":"y
    10."stalk-shape:"              enlarging":"e","tapering":"t
    11."stalk-root:"               bulbous":"b","club":"c","cup":"u","equal":"e","
                                  rhizomorphs":"z","rooted":"r","missing":"?
    12."stalk-surface-above-ring:" fibrous":"f","scaly":"y","silky":"k","smooth":"s
    13."stalk-surface-below-ring:" fibrous":"f","scaly":"y","silky":"k","smooth":"s
    14."stalk-color-above-ring:"   brown":"n","buff":"b","cinnamon":"c","gray":"g","orange":"o","
                                  pink":"p","red":"e","white":"w","yellow":"y
    15."stalk-color-below-ring:"   brown":"n","buff":"b","cinnamon":"c","gray":"g","orange":"o","
                                  pink":"p","red":"e","white":"w","yellow":"y
    16."veil-type:"                partial":"p","universal":"u
    17."veil-color:"               brown":"n","orange":"o","white":"w","yellow":"y
    18."ring-number:"              none":"n","one":"o","two":"t
    19."ring-type:"                cobwebby":"c","evanescent":"e","flaring":"f","large":"l","
                                  none":"n","pendant":"p","sheathing":"s","zone":"z
    20."spore-print-color:"        black":"k","brown":"n","buff":"b","chocolate":"h","green":"r","
                                  orange":"o","purple":"u","white":"w","yellow":"y
    21."population:"               abundant":"a","clustered":"c","numerous":"n","
                                  scattered":"s","several":"v","solitary":"y
    22."habitat:"                  grasses":"g","leaves":"l","meadows":"m","paths":"p","
                                  urban":"u","waste":"w","woods":"d
"""