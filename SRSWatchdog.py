#!/usr/bin/env python3

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="DAMICDrone",
  password="Modane00",
  database="DAMICDrone"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT SystemState FROM SMState ORDER BY IDX DESC LIMIT 1")

#mycursor.execute("DESCRIBE SMState")


for x in mycursor:
  print(x) 