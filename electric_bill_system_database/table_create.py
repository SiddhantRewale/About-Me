import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
a=my_db.cursor()
a.execute("create database if not exists Electricity_bill_system") 
a.execute("use Electricity_bill_system")
a.execute("create table if not exists admin(admin_name varchar(100),Password varchar(10),zone_id int primary key,zone_name varchar(100))")
a.execute("create table if not exists consumer(consumer_name varchar(100) NOT NULL,Password varchar(10),consumer_id int primary key auto_increment,zone_id int,address varchar(200) NOT NULL,mobile_no varchar(200) NOT NULL,date_of_connection DATETIME DEFAULT CURRENT_TIMESTAMP,foreign key (zone_id) references admin(zone_id))")
a.execute("alter table consumer auto_increment=10000")
a.execute("create table if not exists bill_transaction(month varchar(255),zone_id int,consumer_id int,meter_reading int,due_bill_amount int,due_date datetime,bill_date datetime,foreign key (zone_id) references admin(zone_id),foreign key (consumer_id) references consumer(consumer_id))")
a.execute("create table if not  exists receipt(zone_id int,consumer_id int,paid_amount int,balance_amount int,Date_of_Transaction DATETIME,foreign key (zone_id) references admin(zone_id),foreign key (consumer_id) references consumer(consumer_id))")




             
              
              
             
             
              

