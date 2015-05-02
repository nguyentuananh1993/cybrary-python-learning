import sqlite3 as lite
import unicodedata, codecs, urllib2
import string
from bs4 import BeautifulSoup

def readSoup(word,proxy):
	proxy_support = urllib2.ProxyHandler({"http":proxy})  
	opener = urllib2.build_opener(proxy_support)  
	url='http://mazii.net/api/mazii/'+word+'/10'  
	page = opener.open(url)  
	contents=page.read()  
	return contents  

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
				print readSoup(row[1].encode("utf-8"),"http://218.97.194.202:80")
			except:
				check = 1
			if check ==1:
				try:
					print readSoup(row[1].encode("utf-8"),"http://111.161.126.99:80")
				except:
					check = 0
	except lite.Error, e:
		print "Error %s" % e.args[0]
		sys.exit()
	finally:
		if con:
			con.close()
main()