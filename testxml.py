#!/usr/bin/python

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("sample.xml")
root = tree.getroot()

# open a file for writing
places = open('/home/roman/parserpython/demo_data.csv', 'w') 

# create the csv writer object
csvwriter = csv.writer(places)

# array for tags
places_data = []
header = set()

for place in root.findall('Place'):	
	for identity in place.findall('Identity'):
		row = {}	
		for placeid in identity.findall('PlaceId'):
			header.add(placeid.tag)
			row[placeid.tag] = placeid.text
			places_data.append(row)
	

for place in root.findall('Place'):		
	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					row2 = {}
					for countrycode in parsed.findall('CountryCode'):
						header.add(countrycode.tag)
						row2[countrycode.tag] = countrycode.text
						places_data.append(row2)


for place in root.findall('Place'):		
	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					row3 = {}
					for streetname in parsed.findall('StreetName'):
						header.add(streetname.tag)
						for basename in streetname.findall('BaseName'):
							row3[streetname.tag] = basename.text
							places_data.append(row3)
	


for place in root.findall('Place'):		
	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					row4 = {}
					for housenumber in parsed.findall('HouseNumber'):
						header.add(housenumber.tag)
						row4[housenumber.tag] = housenumber.text
						places_data.append(row4)

#2016_09_27/23:38
with open('out.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(header))
    writer.writeheader()
    writer.writerows(places_data)
