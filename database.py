import sqlite3 as lite
def main():
	con = None
	try:
		con = lite.connect("javn.db")
		cur = con.cursor()
		cur.execute('UPDATE kanji SET detail= \"1\" WHERE id=3')
		con.commit()
	except:
		print "error"
	finally:
		if con:
			con.close()