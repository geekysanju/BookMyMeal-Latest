import MySQLdb

db=MySQLdb.connect('localhost','root','','food')

cursor=db.cursor()

print('connection done....')
