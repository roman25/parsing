#!/usr/bin/python

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("sample.xml")
root = tree.getroot()

# open a file for writing
places = open('/home/roman/parserpython/places.csv', 'w') 

# create the csv writer object
csvwriter = csv.writer(places)

# array for tags
places_data = []

count = 0
for place in root.findall('Place'):
	places_text = []
	if count == 0:
		for identity in place.findall('Identity'):
			placeid = identity.find('PlaceId').tag
			places_data.append(placeid)

		for locationlist in place.findall('LocationList'):
			for location in locationlist.findall('Location'):
				for address in location.findall('Address'):
					for parsed in address.findall('Parsed'):
						countrycode = parsed.find('CountryCode').tag
						places_data.append(countrycode)

						streetname = parsed.find('StreetName').tag
						places_data.append(streetname)
																		
						housenumber = parsed.find('HouseNumber').tag
						places_data.append(housenumber)


						for admin in parsed.findall('Admin'):
							for adminlevel in admin.findall('AdminLevel'):
								level1 = adminlevel.find('Level1').tag
								level2 = adminlevel.find('Level2').tag
								level3 = adminlevel.find('Level3').tag
								level4 = adminlevel.find('Level4').tag

								places_data.append(level1)
								places_data.append(level2)
								places_data.append(level3)
								places_data.append(level4)
								

				for geopositionlist in location.findall('GeoPositionList'):
					for geoposition in geopositionlist.findall('GeoPosition'):
						latitude = geoposition.find('Latitude').tag
						longitude = geoposition.find('Longitude').tag
						places_data.append(latitude)
						

						places_data.append(longitude)
						

		for contactlist in place.findall('ContactList'):
			for contact in contactlist.findall('Contact'):
				phone = contact.get('type')
				places_data.append(phone)
				

				webaddress = contact.get('type') # make webaddress
				places_data.append(webaddress)
				

		for namelist in place.findall('NameList'):
			for name in namelist.findall('Name'):
				for textlist in name.findall('TextList'):
					for text in textlist.findall('Text'):
						for basetext in text.findall('BaseText'):
							official = basetext.get('type')
							places_data.append(official)
							
		csvwriter.writerow(places_data)
		#for categorylist in place.findall('CategoryList'):
		#	for category in categorylist.findall('Category'):		
		#		categoryname = category.find('CategoryName').tag #make categoryname
		#		print categoryname
		count = count + 1
	for identity in place.findall('Identity'):
			placeid = identity.find('PlaceId').text
			places_text.append(placeid)
			
	
	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					countrycode = parsed.find('CountryCode').text
					places_text.append(countrycode)

					for streetname in parsed.findall('StreetName'):
						basename = streetname.find('BaseName').text
						places_text.append(basename)

					
					for housnumber in parsed.findall('HouseNumber'):
						housenumber = parsed.find('HouseNumber').text
						places_text.append(housenumber)

					for admin in parsed.findall('Admin'):
						for adminlevel in admin.findall('AdminLevel'):
							level3 = adminlevel.find('Level3').text
							print level3
#last
	csvwriter.writerow(places_text)
	
