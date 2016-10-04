import xml.etree.ElementTree as ET
import csv

tree = ET.parse("sample.xml")
root = tree.getroot()

levels_data = []
names_data = []


header_levels = set()
header_names = set()

for place in root.findall('Place'):
    row_levels = {}
    row_names = {}
    for locationlist in place.findall('LocationList'):
        for location in locationlist.findall('Location'):
            for address in location.findall('Address'):
                for parsed in address.findall('Parsed'):
                    for admin in parsed.findall('Admin'):
                        for adminlevel in admin.findall('AdminLevel'):
                            for level1 in adminlevel.findall('Level1'):
                                header_levels.add(level1.tag)
                                row_levels[level1.tag] = level1.text
                            for level2 in adminlevel.findall('Level2'):
                                header_levels.add(level2.tag)
                                row_levels[level2.tag] = level2.text
                            for level3 in adminlevel.findall('Level3'):
                                header_levels.add(level3.tag)
                                row_levels[level3.tag] = level3.text
                            for level4 in adminlevel.findall('Level4'):
                                header_levels.add(level4.tag)
                                row_levels[level4.tag] = level4.text


    for locationlist in place.findall('LocationList'):
        for location in locationlist.findall('Location'):
            for address in location.findall('Address'):
                for parsed in address.findall('Parsed'):
                    for admin in parsed.findall('Admin'):
                        for adminname in admin.findall('AdminName'):
                            for level1 in adminname.findall('Level1'):
                                header_names.add(level1.tag)
                                row_names[level1.tag] = level1.text
                            for level2 in adminname.findall('Level2'):
                                header_names.add(level2.tag)
                                row_names[level2.tag] = level2.text
                            for level3 in adminname.findall('Level3'):
                                header_names.add(level3.tag)
                                row_names[level3.tag] = level3.text
                            for level4 in adminname.findall('Level4'):
                                header_names.add(level4.tag)
                                row_names[level4.tag] = level4.text



                                
    levels_data.append(row_levels)
    names_data.append(row_names)
with open('levelsadmin.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(header_levels))
    writer.writeheader()
    writer.writerows(levels_data)

with open('namesadmin.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(header_names))
    writer.writeheader()
    writer.writerows(names_data)
