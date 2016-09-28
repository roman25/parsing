#!/usr/bin/python

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("sample.xml")
root = tree.getroot()

# array for tags
places_data = []
header = set()

for place in root.findall('Place'):
	for identity in place.findall('Identity'):
		row0 = {}
		for placeid in identity.findall('PlaceId'):
			header.add(placeid.tag)
			row0[placeid.tag] = placeid.text
			places_data.append(row0)
for place in root.findall('Place'):
	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					row1 = {}
					for countrycode in parsed.findall('CountryCode'):
						header.add(countrycode.tag)
						row1[countrycode.tag] = countrycode.text
						places_data.append(row1)
#number of tags
print len(header)

a = set('hello')
print a
print "len is ", len(a)

for place in root.findall('Place'):
	for categorylist in place.findall('CategoryList'):
		for category in categorylist.findall('Category'):
			findplace = category.get('categorySystem')
			header.add(findplace)
			row10 = {}
			for categoryid in category.findall('CategoryId'):
				row10[findplace] = categoryid.text
				places_data.append(row10)




with open('Stat.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(header))
    writer.writeheader()
    writer.writerows(places_data)
