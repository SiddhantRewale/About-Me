
import mysql.connector
import cons_trans
import cons_bill_detail
#import maskpass
my_db=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
a=my_db.cursor()
a.execute("use Electricity_bill_system")

def consumer(): 
    try:
        while True:
            consumer_no=int(input("Enter a consumer_id: "))
            a.execute("select consumer_id from consumer where consumer_id=%s",[consumer_no])
            p=a.fetchall()
            if consumer_no==p[0][0]:
                break
            else:
                print()
                print("Invalid consumer_id")
                print()
        a.execute("select Password from consumer where consumer_id=%s",[consumer_no])
        p1=a.fetchall()
        while True:
            #pin=maskpass.advpass()
            pin=input("Enter the Password: ")
            if len(pin)==4 and pin.isnumeric():
                if pin==p1[0][0]:
                    break
                else:
                    print()
                    print("INVALID PASSWORD PLEASE TRY AGAIN!!!")
                    print()
            else:
                print()
                print("Enter a valid 4 digit pin")
                print()
            
            
        while True:
            def opt():   
                print("1.Bill Details\n2.Payment option\n3.Exit")
            opt()
            choice = input("Enter your choice : ") 
            if(choice=='1'):
                cons_bill_detail.check_user_bill() 
                
            elif(choice=='2'):
                cons_trans.transaction()
                
            elif(choice=='3'):
                break
            else:
                print("invalid choice")
        my_db.commit()
    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        print("\n")
        my_db.rollback()
