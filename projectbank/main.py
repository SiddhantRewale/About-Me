import acc_opening
import deposit
import withdraw
import balance
import passbookprint
while True :
    def mymain():   
        print("1.Open Account\n2.Deposit Amount\n3.Withdraw Amount\n4.check balance\n5.passbook print\n6.Exit")
    mymain()
    choice = input("Enter your choice : ") 
    if(choice=='1'):
        acc_opening.OpenAccount() 
    elif(choice=='2'):
        deposit.DepositAmount()
    elif(choice=='3'):
        withdraw.WithdrawAmount()
    elif(choice=='4'):
        balance.BalanceCheck()
    elif(choice=='5'):
        passbookprint.pbprint()
        print("\n")  
    elif(choice=='6'):
            break
    else:
        print("\n")
        print("invalid choice")
        print("\n")
        