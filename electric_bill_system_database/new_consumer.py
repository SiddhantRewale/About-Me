
#from tabulate import tabulate
#import pandas as pd
import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
a=my_db.cursor()
a.execute("use Electricity_bill_system")

def add_new_consumer():
    try:
        q="insert into consumer(consumer_name,Password,zone_id,address,mobile_no,date_of_connection)values(%s,%s,%s,%s,%s,now())"
        while True:
                name=input("Enter a name: ")
                if name.isalpha()==False:
                    print("\n")
                    print("Please enter a valid name!!!")
                    print("\n")
                else:
                    break
        while True:
            pin= input("Enter a new pin: ")
            if len(pin)==4 and pin.isnumeric():
                break
            else:
                print("\n")
                print("Enter a valid 4 digit pin")
                print("\n")

        while True:
            print("Please select zone_id are given below:\n 1.1521 for N-ward\n 2.3306 for S-ward \n 3.5432 for A-ward \n 4.8501 for T-ward \n")
            zone_no=int(input("Enter a zone_id: "))
            a.execute("select zone_id from admin where zone_id=%s",[zone_no])
            p=a.fetchall()
            if zone_no==p[0][0]:
                break
            else:
                print("\n") 
                print("Invalid zone_id")
                print("\n") 

        add=input("Enter an address: ")
        while True:
                mob=input("Enter a mobile_no: ")
                if len(mob)==10 and mob.isnumeric():
                    break
                else:
                    print("\n")
                    print("Please enter a valid mobile number!!!")
                    print("\n")
        all=(name,pin,zone_no,add,mob)
        a.execute(q,all)
        a.execute("select consumer_id,consumer_name,zone_id,address,mobile_no,date_of_connection from consumer")
        display=a.fetchall()
        
        """ df=pd.DataFrame(display,columns=[ "consumer_id","name_of_account_holder","zone_id","address","mobile_no","date_of_acc_opening"])
        print(tabulate(df,headers='keys',tablefmt='grid')) """
        details=["consumer_id: ","name_of_account_holder: ","zone_id: ","address: ","mobile_no: ","date_of_acc_opening: "]
        print("\n")
        for i,j in zip(details,display[-1]):
            print(i,j)
        # print(display[-1])
        print("\n")
        my_db.commit()
    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        print("\n")
        
