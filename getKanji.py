# -*- coding: utf-8 -*-
import unicodedata, codecs, urllib2
import string
from bs4 import BeautifulSoup

def readSoup(url):
	url = "http://" + url
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	soup=BeautifulSoup(response,'html.parser')
	return soup

if __name__ == '__main__':
	#resource_file = open('kanji.csv', 'r')
	#result_file = open('listKanji.csv', 'w')
	step = 1
	#for line in resource_file:
	urlkanji = "mazii.net/api/mazii/" + "亜" + "/10"
	#tmp = readSoup(urlkanji).body.findAll('td')
	tmp = readSoup(urlkanji)
	tmp = str(tmp)
		
		# writeline = line[:-1]+';'+tmp+'\n'
		
		# result_file.write(writeline)
	print step 
		#print writeline
	print tmp

	#	step = step + 1

	#resource_file.close()
	#result_file.close()
