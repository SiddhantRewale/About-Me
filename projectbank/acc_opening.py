import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
s=mydb.cursor()
s.execute("use passbook")
def OpenAccount(): 
    try:
        while True:
            name=input("Enter a name: ")
            if name.isalpha()==False:
                print()
                print("Please enter a valid name!!!")
                print()
            else:
                break
        while True:
            pin= input("Enter a new pin: ")
            if len(pin)==4 and pin.isnumeric():
                break
            else:
                print()
                print("Enter a valid 4 digit pin")
                print()
        
        add=input("Enter an address: ")
        while True:
                mob=input("Enter a mobile_no: ")
                if len(mob)==10 and mob.isnumeric():
                    break
                else:
                    print()
                    print("Please enter a valid mobile number!!!")
                    print()
        all=(name,pin,add,mob)
        q="insert into account(name,Password,address,mobile_no,date_of_acc_opening)values(%s,%s,%s,%s,now())"
        s.execute(q,all)
        s.execute("select acc_no,name,address,mobile_no,date_of_acc_opening from account")
        display=s.fetchall()
        details=["accont_no: ","name_of_account_holder: ","address: ","mobile_no: ","date_of_acc_opening: "]
        print("\n")
        for i,j in zip(details,display[-1]):
            print(i,j)
        # print(display[-1])
        print("\n")
        mydb.commit()
    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        print("\n")
        mydb.rollback()

