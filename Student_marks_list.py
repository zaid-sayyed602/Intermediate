student=[]
choice=0
while(choice!=6):
    print("1.Add Student")
    print("2.REMOVE Student")
    print("3.Highest Student Name")
    print("4.Last Student Name")
    print("5.Show all students")
    print("6.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        n=int(input("Enter the no of students you want to add\n"))
        for i in range(n):
            name=input("Enter the name of the student\n")
            rollno=int(input("Enter the roll no of\n"))
            marks=int(input("Enter the marks no of\n"))
            temp=[name,rollno,marks]
            student.append(temp)
    elif(choice==2):
        studremove=input("Enter the student you want to remove\n")
        flag=0
        for i in range(len(student)):
            if(studremove==student[i][0]):
                student.remove(student[i])
                flag=1
                print("removed successfully")
                break
        if(flag==0):
            print("student not found")
    elif(choice==3):
        k=0
        pos=0
        for i in range(len(student)):
            if(k<student[i][2]):
                k=student[i][2]
                pos=i
        print("highest marks scored by the student",student[pos][0])        

    elif(choice==4):
        k=student[i][0]
        pos=0
        for i in range(len(student)):
            if(k>student[i][2]):
                k=student[i][2]
                pos=i
            print("lowest marks scored by the student is",student[pos][0])    


                    
    elif(choice==5):
        for i in range(len(student)):
            print(i+1,student[i])
