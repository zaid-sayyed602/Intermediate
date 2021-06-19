students={}
choice=0
while(choice!=4):
    print("1.ADD")
    print("2.REMOVE")
    print("3.TOPPERS OF GIVEN SUBJECT")
    print("4.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        n=int(input("Enter the no of students you want\n"))
        for i in range(n):
            keys=int(input("Enter the roll no of the student\n"))
            name=input("Enter the name of the student\n")
            temp=[name]
            marks={}
            marks["m1"]=int(input("Enter the marks of M1\n"))
            marks["m2"]=int(input("Enter the marks of M2\n"))
            marks["m3"]=int(input("Enter the marks of M3\n"))
            temp.append(marks)
            values=temp
            students[keys]=values
            print(students)
        print("STUDENTS ADDED SUCCESSFULLY\n")
        print(students)
    elif(choice==2):
        datarem=int(input("Enter the roll no you want to remove\n"))
        students.pop(datarem)
        print("Students removed successfully\n")
    elif(choice==3):
        sub=input("Enter the subject\n")
        high=0
        for keys,values in students.items():
            if(high<values[1][sub]):
                high=values[1][sub]
                name=values[0]
                rollno=keys
        print("topper of given subject",sub,"is",name,"whose roll no is",keys,"and marks are",high)
    elif(choice==4):
        print("EXITED")
