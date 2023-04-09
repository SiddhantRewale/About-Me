import mysql.connector
import maskpass
mydb=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
s=mydb.cursor()
s.execute("use passbook")
def WithdrawAmount(): 
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
        wdraw=int(input("enter a withdraw amount: "))
        wi="select balance from amount where account_no=%s"
        s.execute(wi,[acc_no1])
        balance=s.fetchall()
        bala=balance[-1]
        if wdraw>0 :
            if bala[0]!=0 and bala[0]>wdraw:
                bal=bala[0]-wdraw
                amt="insert into amount(account_no,withdraw,balance,Date_of_Transaction)values(%s,%s,%s,now())"
                s.execute(amt,[acc_no1,wdraw,bal])
                print("\n")
                print("Your TRNASACTION is successful")
                print("\n")
            else:
                print("\n")
                print("Balance is insufficient")
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
        
        