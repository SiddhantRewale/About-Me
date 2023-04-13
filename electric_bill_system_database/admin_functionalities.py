
import mysql.connector
import gene_bill
import payment_option
#import maskpass
my_db=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
a=my_db.cursor()
a.execute("use Electricity_bill_system")

def zone_admin(): 
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
        a.execute("select Password from admin where zone_id=%s",[zone_no])
        p1=a.fetchall()
        while True:
            #pin=maskpass.advpass()
            pin=input("Enter the password: ")
            if len(pin)==4 and pin.isnumeric():
                if pin==p1[0][0]:
                    break
                else:
                    print("\n")
                    print("INVALID PASSWORD PLEASE TRY AGAIN!!!")
                    print("\n")
            else:
                print("\n")
                print("Enter a valid 4 digit pin")
                print("\n")
            
            
        while True:
            def opt():   
                print("1.Generate Bill\n2.check consumer transaction\n3.Exit")
            opt()
            choice = input("Enter your choice : ") 
            if(choice=='1'):
                gene_bill.generate_bill()
            elif(choice=='2'):
                payment_option.check_transaction() 
            elif(choice=='3'):
                break
            else:
                print("\n")
                print("invalid choice")
                print("\n")
        my_db.commit()
    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        print("\n")
        my_db.rollback()
