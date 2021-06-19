list1=[]
n=int(input("enter the number of items you want\n"))
for i in range(n):
    itemadd=input("enter the items you want to add\n")
    list1.append(itemadd)
print("item added sucessfully\n")
n=len(list1)
print("length of the list is",n,"\n")
for i in range(n):
    print(i+1,list1[i])
    print()
olditem=input("enter the name of item you want to replace with\n")
pos=list1.index(olditem)
newitem=input("enter the name of the new item you want")
list1[pos]=newitem
print()
print()
for i in range(n):
    print(i+1,list1[i])

    
