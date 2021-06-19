list1=[]
n=int(input("how many items to add\n:"))
print("name of the item\n")
for i in range(n):
    item=input(i+1)
    list1.append(item)
print(list1)
itemrem=input("name of the item to remove\n:")
list1.remove(itemrem)
print(list1)
