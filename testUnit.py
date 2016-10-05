import unittest
import xml.etree.ElementTree as ET
from collections import Counter

class TestForXML(unittest.TestCase):
    tree = ET.parse("sample.xml")
    root = tree.getroot()
    def test_num_tags(self):
        tree = ET.parse("sample.xml")
        root = tree.getroot()
        numberOfTags = []
        for place in root:
            for contactlist in place.findall('ContactList'):
                for contact in contactlist.findall('Contact'):
                    phone = contact.get('type')
                    numberOfTags.append(phone)


            for locationlist in place.findall('LocationList'):
                for location in locationlist.findall('Location'):
                    for geopositionlist in location.findall('GeoPositionList'):
                        for geoposition in geopositionlist.findall('GeoPosition'):
                            for latitude in geoposition.findall('Latitude'):
                                numberOfTags.append(latitude.tag)
                            for longitude in geoposition.findall('Longitude'):
                                numberOfTags.append(longitude.tag)    
                            for altitude in geoposition.findall('Altitude'):
                                numberOfTags.append(altitude.tag)

                    for address in location.findall('Address'):
                        for parsed in address.findall('Parsed'):
                            for countrycode in parsed.findall('CountryCode'):
                                numberOfTags.append(countrycode.tag)
                            for streetname in parsed.findall('StreetName'):
                                numberOfTags.append(streetname.tag)
	
                            for housenumber in parsed.findall('HouseNumber'):
                                numberOfTags.append(housenumber.tag)

                            for postalcode in parsed.findall('PostalCode'):
                                numberOfTags.append(postalcode.tag)

                            for streetname in parsed.findall('StreetName'):
                                for streettype in streetname.findall('StreetType'):
                                    numberOfTags.append(streettype.tag)
                                    
                            for streetname in parsed.findall('StreetName'):
                                for suffix in streetname.findall('Suffix'):
                                    numberOfTags.append(suffix.tag)
                                    
                            for admin in parsed.findall('Admin'):
                                for adminlevel in admin.findall('AdminLevel'):
                                    for level1 in adminlevel.findall('Level1'):
                                        numberOfTags.append(level1.tag)
                                    for level2 in adminlevel.findall('Level2'):
                                        numberOfTags.append(level2.tag)
                                    for level3 in adminlevel.findall('Level3'):
                                        numberOfTags.append(level3.tag)
                                    for level4 in adminlevel.findall('Level4'):
                                        numberOfTags.append(level4.tag)


            for categorylist in place.findall('CategoryList'):
                for category in categorylist.findall('Category'):
                    fd = category.get('categorySystem')
                    for categoryid in category.findall('CategoryId'):
                        numberOfTags.append(categoryid.tag)
                    numberOfTags.append(category.tag)
                    nameCategory = category.get('categorySystem')
                    for categoryname in category.findall('CategoryName'):
                        numberOfTags.append(categoryname.tag)


            for namelist in place.findall('NameList'):
                for name in namelist.findall('Name'):
                    for textlist in name.findall('TextList'):
                        for text in textlist.findall('Text'):
                            for basetext in text.findall('BaseText'):
                                official = basetext.get('type')
                                numberOfTags.append(official)


            for identity in place.findall('Identity'):
                for timestamp in identity.findall('TimeStamp'):
                    numberOfTags.append(timestamp.tag)
                for placeid in identity.findall('PlaceId'):
                    numberOfTags.append(placeid.tag)

            
            mytags = set(numberOfTags)
            
            for locationlist in place.findall('LocationList'):
                for location in locationlist.findall('Location'):
                    for address in location.findall('Address'):
                        for parsed in address.findall('Parsed'):
                           for admin in parsed.findall('Admin'):           
                                for adminname in admin.findall('AdminName'):
                                    for level1 in adminname.findall('Level1'):
                                        mytags.add(level1.tag)
                                    for level2 in adminname.findall('Level2'):
                                        mytags.add(level2.tag)
                                    for level3 in adminname.findall('Level3'):
                                        mytags.add(level3.tag)
                                    for level4 in adminname.findall('Level4'):
                                        mytags.add(level4.tag)





       
        
        print (mytags)
        q = len((mytags))
        self.assertEqual(q, 26)
        

    def test_uniq(self):
        tree = ET.parse("sample.xml")
        root = tree.getroot()
        categoryid_array = []
        for place in root.findall('Place'):
            for categorylist in place.findall('CategoryList'):
                for category in categorylist.findall('Category'):
                    fd = category.get('categorySystem')
                    for categoryid in category.findall('CategoryId'):
                        if (fd == 'find-places'):
                            categoryid_array.append(categoryid.text)
                        if (fd == 'places-cat'):
                            categoryid_array.append(categoryid.text)
                        if (fd == 'poi'):
                            categoryid_array.append(categoryid.text)

        data = {}
        for i in range(len(categoryid_array)):
            count = 0
            for j in range(len(categoryid_array)):
                if (categoryid_array[i] == categoryid_array[j]):
                    count = count + 1
                    data[categoryid_array[i]] = count
        
        data = set(data)       
        data_len = len(data)
        self.assertEqual(data_len, 9)


if __name__ == '__main__':
    unittest.main()


