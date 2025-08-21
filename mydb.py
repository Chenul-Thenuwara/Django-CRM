import mysql.connector

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Helsinki"
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE!")
