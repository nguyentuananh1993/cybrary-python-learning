import requests
from bs4 import BeautifulSoup

def trade_spider():
	f = open('text.txt', 'w+')
	url = 'http://mazii.net/#search/k/%E5%90%88'
	source_code = requests.get(url)
	plain_text = source_code.text
	print plain_text
	f.write(plain_text.encode("utf-8"))
	f.close();
	# result = plain_text.findAll("div", {"class":"widget-container kanji-detail-fix-height"})
trade_spider()
