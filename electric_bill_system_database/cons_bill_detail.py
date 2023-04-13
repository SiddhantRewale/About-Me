#from tabulate import tabulate
#import pandas as pd
import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
a=my_db.cursor()
a.execute("use Electricity_bill_system")


def check_user_bill():
    try:
        query="SELECT * FROM bill_transaction where zone_id=%s and consumer_id=%s and month=%s"
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
        
        month=input("Enter the bill month in monthyear(like March2023): ")
        all=(zone_no,consumer_no,month)
        a.execute(query,all)
        #print(a.fetchall())
        details= a.fetchall()
        """ df=pd.DataFrame(details,columns=["month", "zone_id", "consumer_id", "meter_reading", "due_bill_amount", "due_date", "bill_date"])
        print(tabulate(df,headers='keys',tablefmt='grid')) """
        display=("month: ", "zone_id: ","consumer_id: ", "meter_reading: ", "due_bill_amount: ", "due_date: ", "bill_date: ")
        print("\n")

        for i,j in zip(display,details[-1]):
            print(i,j)
        # print(display[-1])
        print("\n")
        my_db.commit()


    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        print("\n")
        my_db.rollback()
