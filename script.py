#!/usr/bin/python

import xml.etree.ElementTree as ET
import csv
from collections import Counter

tree = ET.parse("sample.xml")
root = tree.getroot()

tags = []
header = set()
header.add('q')
header.add('w')

for place in root.findall('Place'):
    for categorylist in place.findall('CategoryList'):
        for category in categorylist:
            fd = category.get('categorySystem')
            #fd = category.findtext('Level4', default='')
           # if (fd == 'places-cat'):
            #    for categoryid in category:
             #      tags.append(categoryid.text)

            if (fd == 'find-places'):
                for categoryid in category:
                    tags.append(categoryid.text)

           # if (fd == 'poi'):
            #    for categoryid in category:
          #          print categoryid.text

tags = ["Bob", "Alex", "Bob", "John"] 
a = Counter(tags)
a.most_common()
#print a

with open('Stat2.csv', 'w') as file:
	file.write( "Often_used_tags:\n")
	for k,v in  a.most_common():	        
	        file.write( "<{}>:\n <{}>\t".format(k,v) )
  #  writer.writeheader()
   # writer.writerows(array)
