import mysql.connector
import pandas as pd 
from tabulate import tabulate
import maskpass
mydb=mysql.connector.connect(host='localhost',user='root',password='S1ddh@nt')
s=mydb.cursor()
s.execute("use passbook")
def pbprint():
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
        p1=s.fetchall()
        while True:
            pin=maskpass.advpass()
            if pin==p1[0][0]:
                break
            else:
                print()
                print("INVALID PASSWORD PLEASE TRY AGAIN!!!")
                print()
        query1="select account_no,withdraw,credit,balance,Date_of_Transaction from amount where account_no=%s"
        s.execute(query1,[acc_no1])
        passbookp=s.fetchall()
        print("\n")
        df=pd.DataFrame(passbookp,columns=['Acc No.','withdraw','credit','balance','Date_of_Transaction'])
        print(tabulate(df,headers='keys',tablefmt="grid"))
        mydb.commit()
    except Exception as e:
        print("\n")
        print("Invalid Entry",e)
        mydb.rollback()
        print("\n")