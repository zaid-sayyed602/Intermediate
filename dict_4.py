shop={"rice":10,"wheat":20,"bread":5,"maida":50,"oats":100}
grocery={}
choice=0
while(choice!=5):
    print("1.ADD GROCERY")
    print("2.REMOVE GROCERY")
    print("3.BILL")
    print("4.PRINT")
    print("5.EXIT")
    choice=int(input("\nEnter your choice\n"))
    if(choice==1):
        n=int(input("Enter the no of items you want\n"))
        for i in range(n):
            key=input("Enter the item you want\n")
            values=int(input("Enter the quantity you want\n"))
            if key in shop:
                grocery[key]=values
            else:
                print("Not in the shop")
        print("ADDED SUCCESSFULLY")
    elif(choice==2):
        datarem=input("Enter the name of the item you want to remove\n")
        if datarem in grocery:
            grocery.pop(datarem)
            print("Removed Successfully")
        else:
            print("Not in the bag")
    elif(choice==3):
        total=0
        for keys,values in grocery.items():
            total=total+values*shop[keys]
        print("YOUR TOTAL BILL IS\n",total)
        #------Another Method-------------
        '''for keys in grocery.keys():
                total=total+grocery[key]*shop[key]
            print(total)'''
    elif(choice==4):
        for keys,values in grocery.items():
            print(keys,values)
            print(shop[keys]*values,"/-")
    elif(choice==5):
        print("EXITED")
