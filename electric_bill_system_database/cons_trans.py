import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
a=my_db.cursor()
a.execute("use Electricity_bill_system")

def transaction():
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

        a.execute("select  sum(due_bill_amount) from bill_transaction where consumer_id=%s and zone_id=%s group by consumer_id ",[consumer_no,zone_no])
        bal=a.fetchall()
        #print(bal)
        a.execute("select sum(paid_amount) from receipt where consumer_id=%s and zone_id=%s group by consumer_id",[consumer_no,zone_no])
        total_paid=a.fetchall()
        #print(total_paid)
        if total_paid==[(None,)] or total_paid==[]:
            balance=bal[0][0]-0
        else:
            balance=bal[0][0]-total_paid[0][0]
        if balance==0:
            print("\n")
            print(" Bill already paid !!!")
            print("\n")
        else:
            print("Total payable amount balance is ",int(balance))
            paid=int(input("Enter the Amount: "))
            if paid>0 and paid<=balance:
                
                a.execute(query,[zone_no,consumer_no,paid,balance])
                a.execute("select sum(paid_amount) from receipt where consumer_id=%s and zone_id=%s group by consumer_id",[consumer_no,zone_no])
                total_paid1=a.fetchall()
                bal1=bal[0][0]-total_paid1[0][0]
                print("\n")
                print("Remaining Amount after transaction is ",int(bal1))
                print("\n")
            else:
                print("\n")
                print("Invalid Amount Enter !!!!")
                print("\n")
        my_db.commit()       
    except Exception as e:
        print("\n")
        print("Invalid Entry ",e)
        print("\n")
        my_db.rollback()






