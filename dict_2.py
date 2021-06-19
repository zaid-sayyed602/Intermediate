d={}
n=int(input("Enter the no of keys you want\n"))
for i in range(n):
    key=int(input("Enter the keys\n"))
    values=input("Enter the values\n")
    d[key]=values
print("Successfully added to dictionary")
# to print keys
'''for key in d.keys():
    print(key)'''
# to print values
'''for key in d.values():
    print(values)'''
#to print items
'''for items in d.items():
    print(items)'''
# to print dictionary is a quality format
for keys,values in d.items():
    print(keys)
    print(values)
