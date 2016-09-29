import xml.etree.ElementTree as ET
import csv

tree = ET.parse("sample.xml")
root = tree.getroot()

tags = {}

for place in root.findall('Place'):
    for categorylist in place.findall('CategoryList'):
        for category in categorylist:
            fd = category.get('categorySystem')
            #fd = category.findtext('Level4', default='')
            if (fd == 'places-cat'):
                for categoryid in category:
                   tags.append(categoryid.text)

          #  if (fd == 'find-places'):
           #     for categoryid in category:
           #         print categoryid.text

           # if (fd == 'poi'):
            #    for categoryid in category:
          #          print categoryid.text

print tags
