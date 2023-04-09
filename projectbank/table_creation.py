import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
s=mydb.cursor()
s.execute("use passbook")
s.execute("create table account (name varchar(200),Password varchar(10),acc_no int primary key auto_increment,address varchar(200),mobile_no varchar(200),date_of_acc_opening DATETIME DEFAULT CURRENT_TIMESTAMP)")
s.execute("alter table account auto_increment=10000")
s.execute("create table amount(account_no int,withdraw int,credit int,balance int,Date_of_Transaction DATETIME DEFAULT CURRENT_TIMESTAMP ,foreign key (account_no) references account(acc_no))")


