import mysql.connector
import maskpass
mydb=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
s=mydb.cursor()
s.execute("use passbook")
def DepositAmount(): 
    try:        
        while True:
            acc_no1=int(input("Enter a acc_no: "))
            s.execute("select acc_no from account where acc_no=%s",[acc_no1])
            p=s.fetchall()
            if acc_no1==p[0][0]:
                break
            else:
                print()
                print("Invalid acc_no")
                print()
        s.execute("select Password from account where acc_no=%s",[acc_no1])
        p=s.fetchall()
        while True:
            pin=maskpass.advpass()
            if pin==p[0][0]:
                break
            else:
                print()
                print("INVALID PASSWORD PLEASE TRY AGAIN!!!")
                print()
        dep=int(input("enter a deposit amount: "))
        bal="select balance from amount where account_no=%s"
        s.execute(bal,[acc_no1])
        balance=s.fetchall()
        if dep>0:   
            if balance!=[]:
                bala=balance[-1]
                balance=bala[0]+dep
                amt="insert into amount(account_no,credit,balance,Date_of_Transaction)values(%s,%s,%s,now())"
                s.execute(amt,[acc_no1,dep,balance])
                print("\n")
                print("Your TRNASACTION is successful")
                print("\n")
            else:
                balance=dep
                amt="insert into amount(account_no,credit,balance,Date_of_Transaction)values(%s,%s,%s,now())"
                s.execute(amt,[acc_no1,dep,balance])
                print("\n")
                print("Your TRNASACTION is successful")
                print("\n")       
        else:
            print("\n")
            print("Please enter valid Amount!!")
            print("\n")
        
        mydb.commit()
    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        mydb.rollback()
        print("\n")
        
        