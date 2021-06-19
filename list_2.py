list1=[]
choice=0
while(choice!=5):
    print("1.Add Element")
    print("2.remove element")
    print("3.print all element")
    print("4.replace with new element")
    print("5.Exit")
    print()
    print()
    choice=int(input("enter your choice\n:"))
    if(choice==1):
        n=int(input("enter the no of elements ypu want\n"))
        print("enter the names of the element\n")
        for i in range(n):
            elename=input(i+1)
            list1.append(elename)
        print("elements added sucessfully\n")
    elif(choice==2):
        elerem=input=("enter the element name you want to remove\n")
        list1.remove(elerem)
        print("element removed sucessfully\n")
    elif(choice==3):
        n=len(list1)
        print("your lenght is",n,"\n\n")
        print(list1,"\n\n")
        for i in range(n):
            print(i+1,list1)
    elif(choice==4):
        oldelement=input("enter the old element to replace with\n:")
        pos=list1.index(oldelement)
        list1[pos]=input("enter the new element youn want\n")
        print()
        print()
    else:
        print("EXITED")

