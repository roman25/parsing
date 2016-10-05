#add second col
for categorylist in place.findall('CategoryList'):
        for category in categorylist.findall('Category'):
            fd = category.get('categorySystem')
            for categoryid in category.findall('CategoryId'):
                header_categoryid.add(categoryid.tag)
                header_categoryid.add('category')
                if (fd == 'find-places'):
                    row_findplaces[categoryid.tag] = categoryid.text
                    row_findplaces['category'] = fd
                if (fd == 'places-cat'):
                    row_placescat[categoryid.tag] = categoryid.text
                    row_placescat['category'] = fd
                if (fd == 'poi'):
                    row_poi[categoryid.tag] = categoryid.text
                    row_poi['category'] = fd
