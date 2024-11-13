import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2107783.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
total_characters = len(tree)
counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    # print(result.text)
    num = int(result.text)
    # print(num)
    nums.append(num)

print('Count:', len(nums))
print('Sum:', sum(nums))
