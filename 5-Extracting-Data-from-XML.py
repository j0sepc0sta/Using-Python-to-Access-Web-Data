#http://py4e-data.dr-chuck.net/comments_1858587.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input ('url: ')
print('Retrieving', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall ('comments/comment')

for item in lst:
    count = count + 1
    t = item.find ('count').text
    total = total + float (t)
    
print ('Count:', count)
print ('Sum:' , total)