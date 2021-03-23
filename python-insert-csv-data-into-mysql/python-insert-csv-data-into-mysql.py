import csv
import mysql.connector

conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='roytuts')

cur = conn.cursor()
file = open('students-header.csv')
csv_data = csv.reader(file)

skipHeader = True

for row in csv_data:
	if skipHeader:
		skipHeader = False
		continue
	cur.execute('INSERT INTO student(student_id, student_name, student_dob, student_email, student_address)' 'VALUES(%s, %s, %s, %s, %s)', row)

conn.commit()

conn.close()
