import admin_functionalities as af
import new_consumer
import consumer_functionalities as cf


while True :
    def opt():   
        print("1.Admin_login\n2.Consumer_login\n3.new consumer\n4.Exit")
    opt()
    choice = input("Enter your choice : ") 
    if(choice=='1'):
        af.zone_admin()
       
    elif(choice=='2'):
        cf.consumer()
    
    elif(choice=='3'):
        new_consumer.add_new_consumer()
        
    elif(choice=='4'):
            break
    else:
        print("\n")
        print("invalid choice")
        print("\n")
        