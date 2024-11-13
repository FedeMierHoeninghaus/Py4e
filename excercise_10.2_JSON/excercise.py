import json
import urllib.request

adress = input('Enter location: ')
print('Retriving', adress)
uh = urllib.request.urlopen(adress)
data = uh.read().decode()

# print(data)
print('Retrived', len(data), 'characters')
info = json.loads(data)
# print(info)
print('Count:', len(info["comments"]))
count = 0
for item in info["comments"]:
    # print('name', item['name'])
    # print('count', item['count'])
    count += item["count"]
print('Sum:', count)
