import sqlite3 as lite
import unicodedata, codecs, urllib2
import string
from bs4 import BeautifulSoup
import json

def readSoup(word,proxy):
	proxy_support = urllib2.ProxyHandler({"http":proxy})  
	opener = urllib2.build_opener(proxy_support)  
	url='http://mazii.net/api/mazii/'+word+'/10'  
	page = opener.open(url)  
	contents=page.read()  
	return contents  


def appendData(conn,curs, item, contents):
	jjob = json.loads(contents)
	# print "DETAIL\n"
	detail =  '\"' + jjob['results'][0]['detail'] +'\"'
	# print detail

	# print "COMPDETAIL\n"
	compDetail = "["
	for compdetail in jjob['results'][0]['compDetail']:
		compDetail += '{\"w\":'
		compDetail += compdetail['w']
		compDetail += '\",\"h\":'
		compDetail += compdetail['h']
		compDetail += '\"}'
	compDetail += ']'
	# print compDetail
	# print "EXAMPLES\n"
	Example = "["
	for example in jjob['results'][0]['examples']:
		Example += '{\"w\":'
		Example += example['w']
		Example += '\",\"p\":'
		Example += example['p']
		Example += '\",\"m\":'
		Example += example['m']
		Example += '\",\"h\":'
		Example += example['h']
		Example += '\"}'
	Example += ']'
	# print Example
	curs.execute('UPDATE kanji SET detail= ?,compDetail= ?, examples = ? WHERE id=?',(detail,compDetail, Example,item,))
	conn.commit()

def main():
	database_name = "javn.db"#str(raw_input("File name: "))
	table_name = "kanji" #str(raw_input("Enter table name: "))
	rows = 1 #int(raw_input("Number of row: "))
	
	fro = int(raw_input("From id: "))
	to = int(raw_input("To id: "))

	con = None
	try:
		check = 0
		count =0
		con = lite.connect(database_name)
		cur = con.cursor()
		cur.execute('select * from '+table_name + ' where id >= '+str(fro)+ " and id < "+str(to))
		data = cur.fetchall()
		for row in data:
			try:
				contents = readSoup(row[1].encode("utf-8"),"http://218.97.194.202:80")
				print contents
				appendData(con,cur,row[0],contents)
			except:
				check = 1
			if check ==1:
				try:
					contents = readSoup(row[1].encode("utf-8"),"http://111.161.126.99:80")
					print contents
					appendData(con,cur,row[0],contents)
					count +=1
					print count
				except:
					check = 0
	except lite.Error, e:
		print "Error %s" % e.args[0]
		sys.exit()
	finally:
		if con:
			con.close()
main()