emp={}
choice=0
while(choice!=7):
    print("1.ADD EMPLOYEE")
    print("2.REMOVE EMPLOYEE")
    print("3.SALARY UPDATE")
    print("4.ATTENDANCE UPDATE")
    print("5.APPRAISAL")
    print("6.PERFORMANCE")
    print("7.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        for i in range(int(input("Enter the no of employee you want\n"))):
            empid=int(input("Enter the unique Id of the employee\n"))
            emp1={}
            name=input("enter your name\n")
            contact=int(input("Enter your contact number\n"))
            if(len(str(contact))==10):
                temp=[name,contact]
                emp1["details"]=temp
                print("\n----Enter the performance of 12 months in percentage----\n")
                per={}
                month=["january","february","march","april","may","june","july","august","september","october","noember","december"]
                temp1={}
                for m in month:
                    temp1[m]=input(m)
                month=temp1
                per=month
                atten={}
                emp1["performance"]=per
                emp1["salary"]=int(input("Enter the salary of Employee\n"))
                print("\n----Enter the attendance of all months out of 26 days----\n")
                temp2={}
                for m1 in month:
                    temp2[m1]=input(m1)
                month=temp2
                atten=month
                emp1["attendance"]=atten
                emp[empid]=emp1
                print("ADDED SUCCESSFULLY\n")
                print("EMPLOYEE ID\n",empid)
                for keys,values in emp[empid].items():
                    print(keys)
                    print(values)
            else:
                print("incorrect contact no")
    elif(choice==2):
        keys=list(emp.keys())
        print("ALL EMPLOYEES",keys)
        emprem=int(input("Enter the empid of the employee\n"))
        if emprem in emp:
            emp.pop(emprem)
            print("Employee removed\n")
            keys=list(emp.keys())
            print("UPDATED EMPLOYEES LIST",keys)
        else:
            print("NO SUCH EMPLOYEE IN THE COMPANY")
    elif(choice==3):
        empid=int(input("Enter the empid of the employee\n"))
        if empid in emp:
            salupd=int(input("Enter by how many percent you want to update employees salary \n"))
            emp[empid]["salary"] += emp[empid]["salary"] * salupd/100
            print("Salary updated successfully")
            print("updated salary is",emp[empid]["salary"])
        else:
            print("NO SUCH EMPLOYEE IN COMPANY")

    elif(choice==4):
        empid=int(input("Enter the empid of the employee\n"))
        if empid in emp:
            attenmon=input("Enter the month \n")
            attenupd=int(input("Enter the days you want to add to the attendance\n"))
            print("employees attendance in",attenmon,"was",emp[empid]["attendance"][attenmon],"days")
            emp[empid]["attendance"][attenmon] += attenupd
            print("ATTENDANCE SUCCESSFULLY UPDATED")
            print(" Updated employees attendance in ",attenmon,"is",emp[empid]["attendance"][attenmon],"days")
        else:
            print("NO SUCH EMPLOYEE IN COMPANY")
    elif(choice==5):
        cnt=0
        cnt1=0
        empid=int(input("enter the empid of an employee\n"))
        if empid in emp:
            for values in emp[empid]["attendance"].values():
                cnt=cnt+values
                attenper=cnt/312*100
            print("The employees yearly percentage of attendance is",attenper,"%")
            for values1 in emp[empid]["performance"].values():
                cnt1=cnt1+values1
                perfper=cnt1/1200*100
            print("The employees yearly percentage of performance is",perfper,"%")    
            if(attenper>=80 and perfper>=80 ):
                print("Employees salary is",emp[empid]["salary"])
                emp[empid]["salary"] += emp[empid]["salary"] * 30/100
                print("Appraisal of 30 precent is given to the employee")
                print("updated salary is",emp[empid]["salary"])
            elif(attenper>=60 and perfper>=60):
                print("Employees salary is",emp[empid]["salary"])
                emp[empid]["salary"] += emp[empid]["salary"] * 25/100
                print("Appraisal of 25 precent is given to the employee")
                print("updated salary is",emp[empid]["salary"])
            elif(attenper>=40 and perfper>=40):
                print("Employees salary is",emp[empid]["salary"])
                emp[empid]["salary"] += emp[empid]["salary"] * 20/100
                print("Appraisal of 20 precent is given to the employee")
                print("updated salary is",emp[empid]["salary"])
            elif(attenper>=30 and perfper>=30):
                print("Employees salary is",emp[empid]["salary"])
                emp[empid]["salary"] += emp[empid]["salary"] * 13/100
                print("Appraisal of 13 precent is given to the employee")
                print("updated salary is",emp[empid]["salary"])
            elif(attenper>=20 and perfper>=20):
                print("Employees salary is",emp[empid]["salary"])
                emp[empid]["salary"] += emp[empid]["salary"] * 9/100
                print("Appraisal of 9 precent is given to the employee")
                print("updated salary is",emp[empid]["salary"])
            elif(attenper>=10 and perfper>=10):
                print("Employees salary is",emp[empid]["salary"])
                emp[empid]["salary"] += emp[empid]["salary"] * 3/100
                print("Appraisal of 3 precent is given to the employee")
                print("updated salary is",emp[empid]["salary"])
            else:
                print("Work hard bro you wont get a appraisal")
        else:
            print("NO SUCH EMPLOYEE")
    elif(choice==6):
        cnt=0
        cnt1=0
        empid=int(input("Enter the empid of the employee\n"))
        if empid in emp:
            for values in emp[empid]["attendance"].values():
                cnt=cnt+values
                attenper=cnt/312*100
            print("\nThe employees yearly percentage of attendance is",attenper,"%\n")
            for values1 in emp[empid]["performance"].values():
                cnt1=cnt1+values1
                perfper=cnt1/1200*100
            print("\nThe employees yearly percentage of performance is",perfper,"%\n")                 
            if(attenper>=80 and perfper>=80):
                print("AS PER YOUR PERFORMANCE AND ATTENDANCE")
                print("YOUR GET RATING 4.5/5")
                print("*****")
            elif(attenper>=60 and perfper>=60 ):
                print("AS PER YOUR PERFORMANCE AND ATTENDANCE")
                print("YOUR GET RATING 4/5")
                print("****")
            elif(attenper>=40 and perfper>=40):
                print("AS PER YOUR PERFORMANCE AND ATTENDANCE")
                print("YOUR GET RATING 3/5")
                print("***")
            elif(attenper>=30 and perfper>=30):
                print("AS PER YOUR PERFORMANCE AND ATTENDANCE")
                print("YOUR GET RATING 2.5/5")
                print("**")
            elif(attenper>=20 and perfper>=20):
                print("AS PER YOUR PERFORMANCE AND ATTENDANCE")
                print("YOUR GET RATING 2/5")
                print("**")
            elif(attenper>=10 and perfper>=10):
                print("AS PER YOUR PERFORMANCE AND ATTENDANCE")
                print("YOUR GET RATING 1/5")
                print("*")
            else:
                print("Work hard bro your rating should be below worst")
        else:
            print("NO SUCH EMPLOYEE")            

    elif(choice==7):
        print("BYE BYE")
        print("----THANKS FOR USING THE PROGRAM----")

    else:
        print("\nEnter the correct choice\n")
