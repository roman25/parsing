import unittest

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
