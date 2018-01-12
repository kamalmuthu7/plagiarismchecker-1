from bs4 import BeautifulSoup

import urllib.request
import re

import urllib.parse

url = 'http://www.ask.com/web?q=articles+about+technology&qsrc=2352&qo=searchSuggestions&o=0&l=dir'

request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request, timeout = 5)
data = response.read()

soup = BeautifulSoup(data,'lxml')
res = []

results = soup.findAll('div', {'class': 'PartialSearchResults-item'})
# print(results)

for result in results:
	a = result.find('p')
	print(a.text)
	# match = re.match(r'/url\?q=(http[^&]+)&', a['href'])
	# url = urllib.parse.unquote(match.group(1))
	# res.append({"name" : name, "url" : url})


# print(res)