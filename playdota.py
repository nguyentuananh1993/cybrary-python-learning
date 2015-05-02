import urllib2  
import sqlite3 as lite
import json
proxy_support = urllib2.ProxyHandler({"http":"http://218.97.194.202:80"})  
opener = urllib2.build_opener(proxy_support)  
url='http://mazii.net/api/mazii/%E8%A1%8C/10'  
page = opener.open(url)  
contents=page.read()
print contents  

jjob = json.loads(contents)
print "DETAIL\n"
print jjob['results'][0]['detail']

print "COMPDETAIL\n"
for compdetail in jjob['results'][0]['compDetail']:
	print compdetail['w'],
	print compdetail['h'],

print "EXAMPLES\n"
for example in jjob['results'][0]['examples']:
	print example['w'],
	print example['p'],
	print example['m'],
	print example['h'],



# try:
# 	check = 0
# 	con = lite.connect("development.sqlite3")
# 	cur = con.cursor()
# 	# cur.execute("UPDATE comments SET body=?,user_id=? WHERE question_id = ?",('anhnt is here','100','1'))
# 	con.commit()
# except lite.Error, e:
# 	print "Error %s" % e.args[0]
# 	sys.exit()
# finally:
# 	if con:
# 		con.close()