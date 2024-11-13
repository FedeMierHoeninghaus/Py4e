# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = 0
total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    tag_to_string = str(tag)
    numbers = re.findall('[0-9]+', tag_to_string)
    # print(numbers)
    for number in numbers:
        count += 1
        total += int(number)
print("Count", count)
print("Total", total)
#  print(tag)
#   #Look at the parts of a tag
#  print('TAG:', tag)
#  print('URL:', tag.get('href', None))
#  print('Contents:', tag.contents[0])
#  print('Attrs:', tag.attrs)
