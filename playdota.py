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
detail =  '\"' + jjob['results'][0]['detail'] +'\"'
print detail

print "COMPDETAIL\n"
compDetail = "["
for compdetail in jjob['results'][0]['compDetail']:
	compDetail += '{\"w\":'
	compDetail += compdetail['w']
	compDetail += '\",\"h\":'
	compDetail += compdetail['h']
	compDetail += '\"}'
compDetail += ']'
print compDetail

print "EXAMPLES\n"
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
print Example



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