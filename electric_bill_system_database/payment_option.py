#from tabulate import tabulate
#import pandas as pd
import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
a=my_db.cursor()
a.execute("use Electricity_bill_system")

def check_transaction():
    try:
        query="insert into receipt(zone_id, consumer_id, paid_amount, balance_amount, Date_of_Transaction) values(%s,%s,%s,%s,now())"
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
                    print()
                    print("Invalid consumer_id")
                    print()
        a.execute("select * from receipt where zone_id=%s and consumer_id=%s ",[zone_no,consumer_no])
        details= a.fetchall()
        """ df=pd.DataFrame(details,columns=[ "zone_id", "consumer_id", "paid_amount", "balance_amount", "Date_of_Transaction"])
        print(tabulate(df,headers='keys',tablefmt='grid'))
         """
        display=["zone_id : ", "consumer_id : ", "paid_amount : ", "balance_amount : ", "Date_of_Transaction : "]
        print("\n")
        for k in details:
            for i,j in zip(display,k):
                print(i,j)
            print("\n")
        # print(display[-1])
        print("\n")
        my_db.commit()


    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        print("\n")
        my_db.rollback()

        
        



    