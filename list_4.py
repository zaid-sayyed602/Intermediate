list1=[]
choice=0

while(choice!=6):
    print("1.Add the number")
    print("2.Maximum of a number")
    print("3.Minimum of a number")
    print("4.Average of a number")
    print("5.Print the list of a number")
    print("6.EXIT\n\n\n")
    choice=int(input("Enter Your choice\n:"))
    if(choice==1):
        n=int(input("Enter how many numbers you want\n:"))
        print("Enter the numbers")
        for i in range(n):
            inputdata=int(input(i+1))
            list1.append(inputdata)
        print("number added successfully")
    elif(choice==2):
        n=len(list1)
        for i in range(n):
            highest=list1[0]
            if(highest<list1[i]):
                highest=list1[i]
        print("highest no is",highest,"\n\n\n")
    elif(choice==3):
        n=len(list1)
        for i in range(n):
            lowest=list1[0]
            if(lowest>list1[i]):
                lowest=list1[i]
        print("lowest no is ",lowest,"\n\n\n")    
    elif(choice==4):
        n=len(list1)
        tlt=0
        for i in range(n):
            tlt=tlt + list1[i]
        avg=tlt/n
        print("average of a list is",avg)
    elif(choice==5):
        n=len(list1)
        print("your lenght of list is",n,"\n\n")
        for i in range(n):
            print(i+1,list1[i],"\n\n\n")
    else:
        print("EXITED")
