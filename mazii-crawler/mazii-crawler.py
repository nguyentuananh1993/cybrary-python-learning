import sqlite3 as lite
import unicodedata, codecs, urllib2
import string
import json
import sys
import traceback
import socket
import timeit
import random



def switchProxy():
	proxy = []
	proxy.append("http://222.255.237.69:3128")
	proxy.append("http://115.84.178.93:3128")
	proxy.append("http://42.112.31.40:1234")
	proxy.append("http://123.30.75.115:80")
	proxy.append("http://118.70.13.161:443")
	proxy.append("http://222.255.27.150:3128")
	proxy.append("http://113.160.48.58:8080")
	proxy.append("http://113.161.77.184:8080")
	proxy_flag = 1
	number = 0
	while proxy_flag ==1:
		if number>=len(proxy):
			number = 0
		try:
			contents = readSoup("%E5%AD%97",proxy[number])
			proxy_flag = 0
			return proxy[number]
		except KeyboardInterrupt:
			sys.exit()
		except:
			print "This proxy "+proxy[number]+" is blocked. Switching to another proxy."
			proxy_flag = 1
			number+=1


def readSoup(word,proxy):
	proxy_support = urllib2.ProxyHandler({"http":proxy})  
	opener = urllib2.build_opener(proxy_support)  
	url='http://mazii.net/api/mazii/'+word+'/10'  
	page = opener.open(url)  
	contents=page.read()  
	return contents  

def getSource(word):
	url='http://mazii.net/api/mazii/'+word+'/10'  
	htmltext = urllib2.urlopen(url).read()
	return htmltext


def appendData(conn,curs, item, contents):
	jjob = json.loads(contents)
	# print "DETAIL\n"
	if jjob['results'][0]['detail'] != None:
		detail =  '\"' + jjob['results'][0]['detail'] +'\"'
	else:
		detail = '\"\"'

	# print "COMPDETAIL\n"
	compDetail = "["
	if jjob['results'][0]['compDetail'] != None:
		for compdetail in jjob['results'][0]['compDetail']:
			compDetail += '{\"w\":\"'
			compDetail += compdetail['w'] if compdetail['w'] else ' '
			compDetail += '\",\"h\":\"'
			compDetail += compdetail['h'] if compdetail['h'] else ' '
			compDetail += '\"}'
		compDetail += ']'

	# print "EXAMPLES\n"
	Example = "["
	if jjob['results'][0]['examples'] != None:
		for example in jjob['results'][0]['examples']:
			Example += '{\"w\":\"'
			# print example['w']
			Example += example['w'] if example['w'] else ' '
			Example += '\",\"p\":\"'
			Example += example['p'] if example['p'] else ' '
			Example += '\",\"m\":\"'
			Example += example['m'] if example['m'] else ' '
			Example += '\",\"h\":\"'
			Example += example['h'] if example['h'] else ' '
			Example += '\"}'
		Example += ']'

	curs.execute('UPDATE kanji SET detail= ?,compDetail= ?, examples = ? WHERE id=?',(detail,compDetail, Example,item,))
	conn.commit()

def main():
	database_name = "javn.db"#str(raw_input("File name: "))
	table_name = "kanji" #str(raw_input("Enter table name: "))
	rows = 1 #int(raw_input("Number of row: "))
	proxy = ""
	initial = 0
	fro = int(raw_input("From id: "))
	to = int(raw_input("To id: "))
	ip = socket.gethostbyname('mazii.net')

	con = None
	try:
		check = 0
		count =0
		con = lite.connect(database_name)
		cur = con.cursor()
		cur.execute('select * from '+table_name + ' where id >= '+str(fro)+ " and id < "+str(to))
		data = cur.fetchall()
		for row in data:
			if initial == 0:
				proxy = switchProxy()
				initial = 1
			check = 0
			while(check!=1):
				try:
					start = timeit.default_timer()
					contents = readSoup(row[1].encode("utf-8"),proxy)
					# print contents
					appendData(con,cur,row[0],contents)
					count +=1
					stop = timeit.default_timer()
					print "Crawl data from http://mazii.net ("+ip+"): data_seq="+ str(count)+" kanji_id="+str(row[0])+" kanji_detail="+str(row[1].encode("utf-8"))+" proxy="+proxy+" ttl="+str(round(stop - start,4))+'s'
					check = 1
				except KeyboardInterrupt:
					sys.exit()
				except urllib2.HTTPError, e:
					proxy = switchProxy()
				except urllib2.URLError, e:
					print "HTTP 404 File Not Found"
				except:
					print sys.exc_info()[0]
	except lite.Error, e:
		print "Error %s" % e.args[0]
		sys.exit()
	finally:
		if con:
			con.close()
main()