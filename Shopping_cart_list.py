shop=[["oil",50],["rice",40],["wheat",60],["oats",100],["corn",50],["maggi",70],["maida",120],["coke",80],["flour",30],["ice",30]]
cart=[]
choice=0
while(choice!=4):
    print("1.ADD ITEMS TO THE CART")
    print("2.REMOVE FORM THE CART")
    print("3.BILL")
    print("4.EXIT")
    choice=int(input("\n\nEnter your choice\n"))
    if(choice==1):
        n=int(input("Enter the no of items you want\n"))
        for i in range(n):
            datainput=input("Enter the name of the items\n")
            flag=0
            for i in range(len(shop)):
                if(datainput==shop[i][0]):
                    cart.append(shop[i])
                    flag=1
                    print("\n\nITEM ADDED SUCCESSFULLY\n")
                    print(cart)
                    break
        if(flag==0):
            print("NOT FOUND")
    elif(choice==2):
        dataremove=input("Enter the name of the item to remove\n")
        flag=0
        for di in cart:
            if(di[0]==dataremove):
                cart.remove(di)
                flag=1
                break
        if(flag==0):
            print("NOT IN THE CART")
        print("\n\nREMOVED SUCCESSFULLY\n")
        print(cart)
    elif(choice==3):
        di=0
        tlt=0
        for i in range(len(cart)):
            tlt += cart[i][1]
        print("YOUR BILL IS ",tlt)
    elif(choice==4):
        print("EXITED")
        
