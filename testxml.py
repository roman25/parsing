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

for place in root.findall('Place'):		
	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for geopositionlist in location.findall('GeoPositionList'):
				for geoposition in geopositionlist.findall('GeoPosition'):
					row5 = {}
					for latitude in geoposition.findall('Latitude'):
						header.add(latitude.tag)
						row5[latitude.tag] = latitude.text
						places_data.append(row5)

					row6 = {}
					for longitude in geoposition.findall('Longitude'):
						header.add(longitude.tag)
						row5[longitude.tag] = longitude.text
						places_data.append(row6)

					row7 = {}
					for altitude in geoposition.findall('Altitude'):
						header.add(altitude.tag)
						row5[altitude.tag] = altitude.text
						places_data.append(row7)


for place in root.findall('Place'):		
	for contactlist in place.findall('ContactList'):
		for contact in contactlist.findall('Contact'):
			phone = contact.get('type')
			header.add(phone)
			row8 = {}
			for contactstring in contact.findall('ContactString'):
				row8[phone] = contactstring.text
				places_data.append(row8)


for place in root.findall('Place'):
	for namelist in place.findall('NameList'):
		for name in namelist.findall('Name'):
			for textlist in name.findall('TextList'):
				for text in textlist.findall('Text'):
					row9 = {}
					for basetext in text.findall('BaseText'):
						official = basetext.get('type')
						header.add(official)
						row9[official] = basetext.text
						places_data.append(row9)


for place in root.findall('Place'):
	for categorylist in place.findall('CategoryList'):
		for category in categorylist.findall('Category'):
			findplace = category.get('categorySystem')
			header.add(findplace)
			row10 = {}
			for categoryid in category.findall('CategoryId'):
				row10[findplace] = categoryid.text
				places_data.append(row10)

			for categoryname in category.findall('CategoryName'):
				row11 = {}
				for textt in categoryname.findall('Text'):
					header.add(textt.tag)	
					row11[textt.tag] = textt.text
					places_data.append(row11)





with open('out.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(header))
    writer.writeheader()
    writer.writerows(places_data)
