student=[]
choice=0
while(choice!=5):
    print("1.Add Student")
    print("2.Remove Student")
    print("3.Toppers of each subject")
    print("4.Total of each Student")
    print("5.Exit")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        n=int(input("Enter the no of students you want\n"))
        for i in range(n):
            name=input("Enter the name of the student\n")
            rollno=int(input("Enter the roll no of the student\n"))
            temp=[name,rollno]
            marks1=int(input("Enter the marks of first subject\n"))
            marks2=int(input("Enter the marks of second subject\n"))
            marks3=int(input("Enter the marks of third subject\n"))
            temp1=[marks1,marks2,marks3]
            temp.append(temp1)
            student.append(temp)
            print(student)
    elif(choice==2):
        remstud=input("Enter the name of the student to remove\n")
        flag=0
        for i in range(len(student)):
            if(remstud==student[i][0]):
                student.remove(student[i])
                flag=1
                print("Removed Successfully")
                break
        if(flag==0):
            print("Student not found")
    elif(choice==3):
        highest=[]
        for i in range(len(student[0][2])):
            highest.append(0)
        for i in range(len(student)):
            for j in range(len(student[i][2])):
                if(highest[j]<student[i][2][j]):
                    highest[j]=student[i][2][j]
                    name=student[i][0]
        print("name of student",name,"marks",highest)
    elif(choice==4):
        for i in range(len(student)):
            tlt=0
            for j in range(len(student[i][2])):
                tlt += student[i][2][j]
                name=student[i][0]
        print("total of ",name,"is",tlt)
            

    elif(choice==5):
        print("EXITED")
