import mysql.connector

mydb = mysql.connector.connect (
  host = "localhost",
  user = "user",
  passwd="pa55w0rd",
  port = "3306"
)

print (mydb)
