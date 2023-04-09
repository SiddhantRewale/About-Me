import mysql.connector
import maskpass
mydb=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
s=mydb.cursor()
s.execute("use passbook")
def BalanceCheck():
    try:
        while True:
            acc_no1=int(input("Enter a acc_no: "))
            s.execute("select acc_no from account where acc_no=%s",[acc_no1])
            p=s.fetchall()
            if acc_no1==p[0][0]:
                break
            else:
                print("Invalid acc_no")
            
        while True:
            pin=maskpass.advpass()
            s.execute("select Password from account where acc_no=%s",[acc_no1])
            p1=s.fetchall()
            if pin==p1[0][0]:
                break
            else:
                print("INVALID PASSWORD PLEASE TRY AGAIN!!!")
                print()
        query1="select balance from amount where account_no =%s order by Date_of_Transaction desc limit 1"
        s.execute(query1,[acc_no1])
        balance=s.fetchall()
        if balance==[]:
            print("\n")
            print('balance is 0')
            print("\n")
        else:
            print("\n")
            print("balance Available is: ",balance[0][0])
            print("\n")
        mydb.commit()      
    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        mydb.rollback()
        print("\n")
            
    
    