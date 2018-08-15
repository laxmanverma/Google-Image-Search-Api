import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getSoupContent(SEARCH_URL):
	hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	req = urllib.request.Request(SEARCH_URL,headers=hdr)
	page = urlopen(req).read()
	soup = BeautifulSoup(page, 'html.parser')
	# print(soup.prettify())
	return soup
