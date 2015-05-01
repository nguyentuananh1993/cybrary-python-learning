import sqlite3 as lite
import unicodedata, codecs, urllib2
import string
from bs4 import BeautifulSoup

def readSoup(url):
	url = "http://" + url
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	soup=BeautifulSoup(response,'html.parser')
	return soup

def main():
	database_name = "javn.db"#str(raw_input("File name: "))
	table_name = "kanji" #str(raw_input("Enter table name: "))
	rows = 1#int(raw_input("Number of row: "))
	con = None
	try:
		check = 0
		con = lite.connect(database_name)
		cur = con.cursor()
		cur.execute('select * from '+table_name)
		data = cur.fetchall()
		for row in data:
			try:
				proxy_support = urllib2.ProxyHandler({"http":"http://218.97.194.202:80"})  
				opener = urllib2.build_opener(proxy_support)  
				url='http://mazii.net/api/mazii/'+row[1].encode("utf-8")+'/10'  
				page = opener.open(url)  
				contents=page.read()  
				print contents  
			except:
				check = 1
			if check ==1:
				try:
					proxy_support = urllib2.ProxyHandler({"http":"http://111.161.126.99:80"})  
					opener = urllib2.build_opener(proxy_support)  
					url='http://mazii.net/api/mazii/'+row[1].encode("utf-8")+'/10'  
					page = opener.open(url)  
					contents=page.read()  
					print contents  
				except:
					check = 0
	except lite.Error, e:
		print "Error %s" % e.args[0]
		sys.exit()
	finally:
		if con:
			con.close()
main()