bank=[]
choice=0
while(choice!=7):
    print("1.ADD")
    print("2.REMOVE")
    print("3.CREDIT")
    print("4.DEBIT")
    print("5.CHECK BALANCE")
    print("6.TRANSFER")
    print("7.EXIT")
    choice=int(input("\nEnter your choice\n"))
    if(choice==1):
        n=int(input("Enter the no of clients you want\n"))
        for i in range(n):
            name=input("Enter your name\n")
            accno=int(input("Enter your account no\n"))
            balance=int(input("Enter your balance\n"))
            pin=int(input("Enter 4 digit pin\n"))
            repin=int(input("Re-Enter your pin\n"))
            if(pin==repin):
                print("CLIENT ADDED SUCCESSFULLY\n")
                temp=[name,accno,balance,pin]
                bank.append(temp)
                print(bank)
            else:
                print("PIN DONT MATCH")
    elif(choice==2):
        clirem=int(input("Enter the accno of the client you want to remove\n"))
        flag=0
        for i in range(len(bank)):
            if(clirem==bank[i][1]):
                bank.remove(bank[i])
                flag=1
                print("REMOVED SUCCESSFULLY")
        if(flag==0):
            print("NO SUCH CLIENT")
        print(bank)
    elif(choice==3):
        accno=int(input("Enter your account no\n"))
        pin=int(input("Enter your pin\n"))
        for i in range(len(bank)):
            if(accno==bank[i][1] and pin==bank[i][3]):
                credit=int(input("Enter the amount you want to credit\n"))
                bank[i][2]+=credit
                print(bank)
    elif(choice==4):                
        accno=int(input("Enter your account no\n"))
        pin=int(input("Enter your pin\n"))
        for i in range(len(bank)):
            if(accno==bank[i][1] and pin==bank[i][3]):
                debit=int(input("Enter the amount you want to withdraw from your account\n"))
                if(bank[i][2]!=0):
                    bank[i][2]-=debit
                    print(bank)
                else:
                    print("Insufficient balance")
    elif(choice==5):
        accno=int(input("Enter the account no\n"))
        pin=int(input("Enter your pin\n"))
        if(accno==bank[i][1] and pin==bank[i][3]):
            for i in range(len(bank)):
                print("Your Account Balance is",bank[i][2])
    elif(choice==6):
        accno=int(input("Enter the account no\n"))
        pin=int(input("Enter your pin\n"))
        for i in range(len(bank)):
            if(accno==bank[i][1] and pin==bank[i][3]):
                amount=int(input("Enter the amount to transfer"))
                transfer=int(input("Enter the bank account no of the reciever\n"))
                for ii in range(len(bank)):
                    if(transfer==bank[ii][1]):
                        bank[ii][2]+=amount
                        print("Amount added to recievers bank",bank[ii][0],"whose account no is",bank[ii][1],"now balance is",bank[ii][2])
                        bank[i][2]-=amount
                        print("Amount debited from senders bank",bank[i][0],"whose account no is",bank[i][1],"now balance is",bank[i][2])
                        break
                break
                        
    elif(choice==7):
        print("EXITED")
