import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'JRM',
	passwd = '7257'
	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE JRM")

print("All Done!")