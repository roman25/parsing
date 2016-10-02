#!/usr/bin/python

import xml.etree.ElementTree as ET
import csv
from collections import Counter

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

		row1 = {}
		for timestamp in identity.findall('TimeStamp'):
			header.add(timestamp.tag)
			row1[timestamp.tag] = timestamp.text
			places_data.append(row1)


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

uniq_id = []
for place in root.findall('Place'):
	for categorylist in place.findall('CategoryList'):
		for category in categorylist:
			fd = category.get('categorySystem')

			if (fd == 'find-places'):
				for categoryid in category:
					uniq_id.append(categoryid.text)

			if (fd == 'poi'):
				for categoryid in category:
					uniq_id.append(categoryid.text)


			if (fd == 'places-cat'):
				for categoryid in category:
					uniq_id.append(categoryid.text)



num_tags = Counter(uniq_id)

with open('out.csv', 'w') as file:
	writer = csv.DictWriter(file, fieldnames=sorted(header))
	writer.writeheader()
	writer.writerows(places_data)


with open('Stat.csv', 'w') as file:
	file.write("Number of tags:\t")
        file.write(str(len(header)))
        file.write("\n")

	file.write("Unique CategoryId:\n")
	for k, v in  num_tags.most_common():	        
		file.write( "{}: {}\n".format(k, v) )





















tags = []
tags.append('shop')
tags.append('9567')
tags.append('600-6900-0096')
tags.append('shop')
tags.append('9567')
tags.append('600-6900-0000')
tags.append('food-drink')
tags.append('5400')
tags.append('600-6300-0066')
tags.append('Restaurant')
tags.append('100-1000-0000')


data = {}


for i in range(len(tags)):
    count = 0
    for j in range(len(tags)-1):
        if (tags[i] == tags[j]):
            count = count + 1
            data[tags[i]] = count
        
print data
