
from datetime import datetime, timedelta
import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
a=my_db.cursor()
a.execute("use Electricity_bill_system")

def generate_bill():
    try:

        while True:
                zone_no=int(input("Enter a zone_id: "))
                a.execute("select zone_id from admin where zone_id=%s",[zone_no])
                p=a.fetchall()
                if zone_no==p[0][0]:
                    break
                else:
                    print("\n") 
                    print("Invalid zone_id")
                    print("\n") 

        while True:
                consumer_no=int(input("Enter a consumer_id: "))
                a.execute("select consumer_id from consumer where consumer_id=%s",[consumer_no])
                p1=a.fetchall()
                if consumer_no==p1[0][0]:
                    break
                else:
                    print("\n")
                    print("Invalid consumer_id")
                    print("\n")

        current_reading = int(input("Enter current reading: "))
        previous_reading = int(input("Enter previous reading: "))
        units_consumed = current_reading - previous_reading # meter reading mai units consumed daalna hai
        if units_consumed <= 100:
            bill_amount = units_consumed * 3.50
        elif units_consumed <= 300:
            bill_amount = 100 * 3.50 + (units_consumed - 100) * 4.00
        else:
            bill_amount = 100 * 3.50 + 200 * 4.00 + (units_consumed - 300) * 5.00 # bill amount in due bill amount

    # Get the current date
        current_date = datetime.now().date()
    # Add 15 days
        new_date = current_date + timedelta(days=15) # new_date in due date
        print("\n")
    # Print the new date
        print("Total electricity bill is: " + str(bill_amount) + " INR")
        print('Due Date: ' + str(new_date))

        

        current_month = datetime.now().date().strftime('%B')
        current_year = datetime.now().date().strftime('%Y')
        my=str(current_month)+str(current_year)
    
             

        query=("insert into bill_transaction(month, zone_id, consumer_id, meter_reading, due_bill_amount, due_date, bill_date) values(%s,%s,%s,%s,%s,%s,now())")
        all=(my,zone_no,consumer_no,units_consumed,bill_amount,new_date)
        a.execute(query,all) 

        a.execute("select * from bill_transaction")
        display=a.fetchall()
        
        details=["month: ", "zone_id: ", "consumer_id: ", "meter_reading: ", "due_bill_amount: ", "due_date: ", "bill_date: "]
        print("\n")
        for i,j in zip(details,display[-1]):
            print(i,j)

        
        print("\n")
        my_db.commit()
    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        print("\n")
        my_db.rollback()



        
   
   
   









