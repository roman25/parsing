#!/usr/bin/python

import xml.etree.ElementTree as ET
import csv
from collections import Counter

tree = ET.parse("sample.xml")
root = tree.getroot()

# array for tags

contact_data = []
geoposition_data = []
categoryid_data = []
categorysystem_data = []
address_data = []
official_data = []
categoryname_data = []
levels_data = []
names_data = []
id_data = []


header_contact = set()
header_geoposition = set()
header_categoryid = set()
header_categorysystem = set()
header_address = set()
header_official = set()
header_categoryname = set()
header_levels = set()
header_names = set()
header_id = set()




for place in root.findall('Place'):

	row_contact = {}
	row_geoposition = {}
	row_categoryid = {}

	row_findplaces = {}
	row_poi = {}
	row_placescat = {}

	row_categorysystem1 = {}
	row_categorysystem2 = {}
	row_categorysystem3 = {}

	row_address = {}
	row_official = {}
	row_categorynamePOI = {}
	row_categorynamePC = {}

	row_levels = {}
	row_names = {}

	row_id = {}



	for contactlist in place.findall('ContactList'):
		for contact in contactlist.findall('Contact'):
			phone = contact.get('type')
			header_contact.add(phone)

			for contactstring in contact.findall('ContactString'):
				row_contact[phone] = contactstring.text


	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for geopositionlist in location.findall('GeoPositionList'):
				for geoposition in geopositionlist.findall('GeoPosition'):

					for latitude in geoposition.findall('Latitude'):
						header_geoposition.add(latitude.tag)
						row_geoposition[latitude.tag] = latitude.text

					for longitude in geoposition.findall('Longitude'):
						header_geoposition.add(longitude.tag)
						row_geoposition[longitude.tag] = longitude.text


					for altitude in geoposition.findall('Altitude'):
						header_geoposition.add(altitude.tag)
						row_geoposition[altitude.tag] = altitude.text



	for categorylist in place.findall('CategoryList'):
		for category in categorylist.findall('Category'):
			fd = category.get('categorySystem')
			for categoryid in category.findall('CategoryId'):
				header_categoryid.add(categoryid.tag)
				if (fd == 'find-places'):
					row_findplaces[categoryid.tag] = categoryid.text
				if (fd == 'places-cat'):
					row_placescat[categoryid.tag] = categoryid.text
				if (fd == 'poi'):
					row_poi[categoryid.tag] = categoryid.text


	for categorylist in place.findall('CategoryList'):
		for category in categorylist.findall('Category'):
			fd = category.get('categorySystem')
			header_categorysystem.add(category.tag)

			if (fd == 'poi'):
				row_categorysystem1[category.tag] = fd

			if (fd == 'find-places'):
				row_categorysystem2[category.tag] = fd

			if (fd == 'places-cat'):
				row_categorysystem3[category.tag] = fd


	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					for countrycode in parsed.findall('CountryCode'):
						header_address.add(countrycode.tag)
						row_address[countrycode.tag] = countrycode.text
	

	
	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					for streetname in parsed.findall('StreetName'):
						header_address.add(streetname.tag)
						for basename in streetname.findall('BaseName'):
							row_address[streetname.tag] = basename.text

	
		
	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					for housenumber in parsed.findall('HouseNumber'):
						header_address.add(housenumber.tag)
						row_address[housenumber.tag] = housenumber.text


	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					for postalcode in parsed.findall('PostalCode'):
						header_address.add(postalcode.tag)
						row_address[postalcode.tag] = postalcode.text


	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					for streetname in parsed.findall('StreetName'):
						for streettype in streetname.findall('StreetType'):
							header_address.add(streettype.tag)
							row_address[streettype.tag] = streettype.text


	for locationlist in place.findall('LocationList'):
		for location in locationlist.findall('Location'):
			for address in location.findall('Address'):
				for parsed in address.findall('Parsed'):
					for streetname in parsed.findall('StreetName'):
						for suffix in streetname.findall('Suffix'):
							header_address.add(suffix.tag)
							row_address[suffix.tag] = suffix.text




	for namelist in place.findall('NameList'):
		for name in namelist.findall('Name'):
			for textlist in name.findall('TextList'):
				for text in textlist.findall('Text'):
					for basetext in text.findall('BaseText'):
						official = basetext.get('type')
						header_official.add(official)
						row_official[official] = basetext.text




	for categorylist in place.findall('CategoryList'):
		for category in categorylist.findall('Category'):
			nameCategory = category.get('categorySystem')
			if nameCategory == 'poi':
				for categoryname in category.findall('CategoryName'):
					header_categoryname.add(categoryname.tag)
					for textt in categoryname.findall('Text'):
						row_categorynamePOI[categoryname.tag] = textt.text


			if nameCategory == 'places-cat':
				for categoryname in category.findall('CategoryName'):
					header_categoryname.add(categoryname.tag)
					for textt in categoryname.findall('Text'):
						row_categorynamePC[categoryname.tag] = textt.text



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


	for identity in place.findall('Identity'):
		for timestamp in identity.findall('TimeStamp'):
			header_id.add(timestamp.tag)
			row_id[timestamp.tag] = timestamp.text

	for identity in place.findall('Identity'):
		for placeid in identity.findall('PlaceId'):
			header_id.add(placeid.tag)
			row_id[placeid.tag] = placeid.text






	contact_data.append(row_contact)
	geoposition_data.append(row_geoposition)
	categoryid_data.append(row_findplaces)
	categoryid_data.append(row_placescat)
	categoryid_data.append(row_poi)
	categorysystem_data.append(row_categorysystem1)
	categorysystem_data.append(row_categorysystem2)
	categorysystem_data.append(row_categorysystem3)
	address_data.append(row_address)
	official_data.append(row_official)
	categoryname_data.append(row_categorynamePOI)
	categoryname_data.append(row_categorynamePC)
	levels_data.append(row_levels)
	names_data.append(row_names)
	id_data.append(row_id)



for x in range(0, 2):
    del categoryname_data[x]


for i in range(0, len(categorysystem_data)-3):
	categorysystem_data.pop()


############################################	STATISTIC	#########################################
#get number of tags for 4.1
fullLenght = []
fullLenght.append(len(header_contact))
fullLenght.append(len(header_geoposition))
fullLenght.append(len(header_categoryid))
fullLenght.append(len(header_categorysystem))
fullLenght.append(len(header_address))
fullLenght.append(len(header_official))
fullLenght.append(len(header_categoryname))
fullLenght.append(len(header_levels))
fullLenght.append(len(header_names))
fullLenght.append(len(header_id))


#get values for 4.2
uniq_id = []
uniq_lc = []
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
#get values for 4.3
	for namelist in place.findall('NameList'):
		for name in namelist.findall('Name'):
			for textlist in name.findall('TextList'):
				for textt in textlist.findall('Text'):
					for basetext in textt.findall('BaseText'):
						lc = basetext.get('languageCode')
						uniq_lc.append(lc)



space = uniq_id[2]
count = len(uniq_id)-1
for x in range(len(uniq_id)-1):
	if uniq_id[count] == space:
		del uniq_id[count]
	count = count-1

num_tags = Counter(uniq_id)
num_lc = Counter(uniq_lc)



####	records to files
with open('files/Stat.csv', 'w') as file:
	file.write("Number of tags:\t")
        file.write(str(sum(fullLenght)))
        file.write("\n")
        file.write("\n")

	file.write("Unique CategoryId:\t\n")
	for k, v in  num_tags.most_common():	        
		file.write( "{}:\t {}\n".format(k, v) )
	file.write("\n")

	file.write("Unique languageCode:\n")
	for k, v in  num_lc.most_common():	        
		file.write( "{}:\t {}\n".format(k, v) )

with open('files/contact.csv', 'w') as file:
	writer = csv.DictWriter(file, fieldnames=sorted(header_contact))
	writer.writeheader()
	writer.writerows(contact_data)

with open('files/geoposition.csv', 'w') as file:
	writer = csv.DictWriter(file, fieldnames=sorted(header_geoposition))
	writer.writeheader()
	writer.writerows(geoposition_data)

with open('files/categoryid.csv', 'w') as file:
	writer = csv.DictWriter(file, fieldnames=sorted(header_categoryid))
	writer.writeheader()
	writer.writerows(categoryid_data)

with open('files/categorysystem.csv', 'w') as file:
	writer = csv.DictWriter(file, fieldnames=sorted(header_categorysystem))
	writer.writeheader()
	writer.writerows(categorysystem_data)

with open('files/address.csv', 'w') as file:
	writer = csv.DictWriter(file, fieldnames=sorted(header_address))
	writer.writeheader()
	writer.writerows(address_data)

with open('files/official.csv', 'w') as file:
	writer = csv.DictWriter(file, fieldnames=sorted(header_official))
	writer.writeheader()
	writer.writerows(official_data)

with open('files/categoryname.csv', 'w') as file:
	writer = csv.DictWriter(file, fieldnames=sorted(header_categoryname))
	writer.writeheader()
	writer.writerows(categoryname_data)


with open('files/levelsadmin.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(header_levels))
    writer.writeheader()
    writer.writerows(levels_data)

with open('files/namesadmin.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(header_names))
    writer.writeheader()
    writer.writerows(names_data)

with open('files/id_data.csv', 'w') as file:
	writer = csv.DictWriter(file, fieldnames=sorted(header_id))
	writer.writeheader()
	writer.writerows(id_data)


