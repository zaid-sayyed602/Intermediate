bank={}
choice=0
while(choice!=7):
    print("1.ADD ACCOUNT")
    print("2.REMOVE ACCOUNT")
    print("3.CREDIT TO ACCOUNT")
    print("4.DEBIT TO ACCOUNT")
    print("5.CHECK BALANCE")
    print("6.TRANSFER TO ACCOUNT")
    print("7.EXIT")
    choice=int(input("\nEnter your choice\n"))
    if(choice==1):
        for i in range(int(input("Enter the no of holders you want\n"))):
            accno=int(input("Enter the account no of holder\n"))
            temp={}
            temp["pin"]=int(input("Enter your 4 digit pin\n"))
            repin=int(input("Enter your pin again\n"))
            if(repin==temp["pin"] and len(str(temp["pin"]))==4) :    
                print("pin confirmed")          
                temp["balance"]=int(input("Enter your balance\n"))
                name=input("Enter your name\n")
                contact=int(input("Enter your contact no\n"))
                if(len(str(contact))==10):
                    temp1=[name,contact]
                    temp["details"]=temp1
                    bank[accno]=temp
                else:
                    print("invalid contact number")
                print("ADDED SUCCESSFULLY")
            else:
                print("your pin doesnot match or it should be of 4 digit")          
        for items in bank.items():    
            print(items)
    elif(choice==2):
        accrmv=int(input("Enter the account number to remove\n"))
        if accno in bank:
            bank.pop(accrmv)
            print("Removed Done")
            for items in bank.items():    
                print(items)
                break
        else:
            print("no such account no")
    elif(choice==3):
        accno=int(input("Enter your account number\n"))
        pin=int(input("Enter your pin\n"))
        if accno in bank and bank[accno]["pin"]==pin:
            print("login successfull")
            print("Your balance is ",bank[accno]["balance"],"\n")
            credit=int(input("Enter the amount you want to credit\n"))
            bank[accno]["balance"]+=credit
            print("Successfully credit to your bank account")
            print("your updated balance is",bank[accno]["balance"],"\n")
        else:
            print("login unsuccessfull")
    elif(choice==4):
        accno=int(input("Enter your account number\n"))
        pin=int(input("Enter your pin\n"))
        if accno in bank and bank[accno]["pin"]==pin:
            print("login successfull")
            print("Your balance is ",bank[accno]["balance"],"\n")
            debit=int(input("Enter the amount you want to credit\n"))
            bank[accno]["balance"]-=debit
            print("Successfully debited from your bank account please collect your cash")
            print("Your updated balance is",bank[accno]["balance"],"\n")
        else:
            print("login unsuccessfull")
        
    elif(choice==5):
        accno=int(input("Enter your account number\n"))
        pin=int(input("Enter your pin\n"))
        if accno in bank and bank[accno]["pin"]==pin:
            print("Login successfull")
            print("YOUR NAME ",bank[accno]["details"][0])
            print("YOUR TOTAL BALANCE IS",bank[accno]["balance"])
        else:
            print("Login unsuccessful")
    elif(choice==6):
        accno=int(input("Enter your account no\n"))
        pin=int(input("Enter your pin"))
        if accno in bank and bank[accno]["pin"]==pin:
            print("login successfull")
            amount=int(input("Enter the amount you want to transfer"))
            bank[accno]["balance"] -= amount
            transfer=int(input("Enter the account no of the recievers bank\n"))
            print("sucessfully transfered from your account it has been debited by",amount,"now your total balance is",bank[accno]["balance"])
            if transfer in bank:
                bank[transfer]["balance"] += amount
                print("Receivers account has been successfully credited by ",amount,"his total balance is",bank[accno]["balance"])
