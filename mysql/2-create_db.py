import mysql.connector

mydb = mysql.connector.connect (
  host = "localhost",
  user = "root",
  passwd="rude_pa55w0rd",
  port = "3306"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
