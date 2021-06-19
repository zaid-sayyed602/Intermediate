grocery={}
choice=0
while(choice!=4):
    print("1.ADD GROCERY")
    print("2.REMOVE GROCERY")
    print("3.PRINT BILL")
    print("4.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        n=int(input("Enter the no of grocery you want\n"))
        for i in range(n):
            key=input("Enter the name of the item\n")
            value=input("Enter the quantity \n")
            grocery[key]=value
        print("Added to bag")
    elif(choice==2):
        datarem=input("Enter the name of the item you want to remove\n")
        if datarem in grocery:
            grocery.pop(datarem)
            print("Removed Successfully")
        else:
            print("Not in the bag")
    elif(choice==3):
        for items in grocery.items():
            print(items)
    elif(choice==4):
        print("EXITED")
        
