import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
s=mydb.cursor()
s.execute("create database passbook")
