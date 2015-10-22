import time
import os
import MySQLdb
import string

while True:
	try:
	   time.sleep(3)
	   db = MySQLdb.connect("localhost","root","root","oj" )
	   cursor = db.cursor()
	   sql = "SELECT * FROM virtualsolution WHERE runid=(SELECT min(runid) FROM virtualsolution WHERE status='Pending')"
           cursor.execute(sql)
           results = cursor.fetchall()
	   db.close()
           if len(results) > 0:
             os.system("python ./judge_client.py")
	except MySQLdb.Error,e:
           print "Mysql Error 1-%d: %s" % (e.args[0], e.args[1])
	   db.close()
           exit(1)

