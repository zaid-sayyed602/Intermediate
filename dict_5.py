students={}
choice=0
while(choice!=4):
    print("1.ADD STUDENTS")
    print("2.REMOVE")
    print("3.TOPPERS")
    print("4.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        n=int(input("Enter the no of students you want\n"))
        for i in range(n):
            keys=int(input("Enter the roll no of the student\n"))
            name=input("Enter the name of the student\n")
            marks=int(input("Enter the marks of the student\n"))
            temp=[name,marks]
            values=temp
            students[keys]=values
        print("ADDED SUCCESFULLY")
        print(students)
    elif(choice==2):
        datarem=int(input("Enter the roll no of the student you want to remove\n"))
        students.pop(datarem)
        print("Removed Successfully")
    elif(choice==3):
        high=0
        for keys,values in students.items():
            if(high>values[1]):
                high=values[1]
                rollno=keys
                name=values[0]
        print("The topper is",name,"whose roll no is",rollno,"and his total is",high)        
    elif(choice==4):
        print("EXITED")
