student=[]
choice=0
while(choice!=7):
    print("1.ADD STUDENTS")
    print("2.REMOVE STUDENTS USING ROLL NO")
    print("3.PRINT LIST OF STUDENTS PRESENT ON MONDAY")
    print("4.PRINT LIST OF STUDENT ABSENT ON WEDNESDAY OR FRIDAY")
    print("5.PRINT LIST OF STUDENT PRESENT ON WEDNESDAY AND THURSDAY")
    print("6.PRINT LIST OF DETAINED STUDENTS")
    print("7.EXIT")
    choice=int(input("\nEnter Your choice\n"))
    if(choice==1):
        n=int(input("Enter the no of student you want\n"))
        for i in range(n):
            name=input("\nEnter the name of the student\n")
            rollno=int(input("Enter the roll no of the student\n"))
            temp=[name,rollno]
            print("please give the input in P=present and A=absent\n")
            mon=input("Was student present or absent on monday\n")
            tue=input("Was student present or absent on tuesday\n")
            wed=input("Was student present or absent on wednesday\n")
            thurs=input("Was student present or absent on thursday\n")
            fri=input("Was student present or absent on friday\n")
            temp1=[mon,tue,wed,thurs,fri]
            temp.append(temp1)
            student.append(temp)
            print("successfully added")
            print(student)
    elif(choice==2):
        remstud=int(input("Enter the roll no of student you want to remove\n"))
        flag=0
        for i in range(len(student)):
            if(remstud==student[i][1]):
                student.remove(student[i])
                flag=1
                break
        if(flag==0):
            print("not found")
        print("REMOVED SUCCESSFULLY\n")    
        print(student)                
    elif(choice==3):
        flag=0
        for i in range(len(student)):
            if(student[i][2][0]=="p"):
                print("students who was present on monday is ",student[i][0])
                flag=1
        if(flag==0):
            print("no one was present on monday")
    elif(choice==4):
        flag=0
        for i in range(len(student)):
            if(student[i][2][2]=="a" or student[i][2][4]=="a"):
                print(student[i][0],"was absent on wednesday or friday")
                flag=1
        if(flag==0):
            print("no one was absent")
    elif(choice==5):
        flag=0
        for i in range(len(student)):
            if(student[i][2][2]=="p" and student[i][2][4]=="p"):
                print(student[i][0],"was absent on wednesday and friday")
                flag=1
        if(flag==0):
            print("no one was absent")
    elif(choice==6):
        for i in range(len(student)):
            count=0
            for j in range(len(student[i][2])):
                if(student[i][2][j]=="a"):
                    count +=1
            if(count>=2):
                print("Detained students are",student[i][0])
            else:
                print("No one is detained")
    elif(choice==7):
        print("EXITED")
