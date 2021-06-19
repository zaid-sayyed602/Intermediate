import pymysql as con
try:
    db=con.connect(
        host="localhost",
        user="root",
        password="root",
        database="shop")
    print("Connection success")
    cur=db.cursor()
except:
    print("something wrong in the connection")
def add(name,quantity):
    select="select * from grocery where item=%s"
    value=[name]
    cur.execute(select,value)
    shop=cur.fetchall()
    select="select * from user where item=%s"
    value=[name]
    cur.execute(select,value)
    cart=cur.fetchall()
    if(len(shop)>0):
        if(len(cart)>0):
            update="update user set quantity=%s where item=%s"
            value=[quantity,name]
            cur.execute(update,value)
            db.commit()
            print("Updated Successfully")
        else:
            insert="insert into user values(%s,%s,%s)"
            value=[0,name,quantity]
            cur.execute(insert,value)
            db.commit()
            print("Successfully added to cart")

    else:
        print("Not in the shop")
def remove(name):
    select="select * from user where item=%s"
    value=[name]
    cur.execute(select,value)
    cart=cur.fetchall()
    for cart1 in cart:
        if(cart[1]==name):
            delete="delete from user where item=%s"
            value=[name]
            cur.execute(delete,value)
            db.commit()
            print("Deleted successfully")

def update(name,quantity):
    select="select * from user"
    cur.execute(select)
    data=cur.fetchall()
    flag=0
    for i in range(len(data)):
        if(data[i][1]==name):
            update="update user set quantity=%s where item=%s"
            value=[quantity,name]
            cur.execute(update,value)
            db.commit()
            print("Updated Successfully")
            flag=1
    if(flag==0):
        print("NOT IN THE CART")
def bill():
    select="select * from grocery"
    cur.execute(select)
    shop=cur.fetchall()
    select="select * from user"
    cur.execute(select)
    cart=cur.fetchall()
    cnt=0
    for i in range(len(cart)):
        for j in range(len(shop)):
            if(cart[i][1]==shop[j][1]):
                cnt+=cart[i][2]*shop[j][2]
                print(cart[i][1],"=",cart[i][2]*shop[j][2],"/-")
                return cnt
choice=0
while(choice!=5):
    print("1.ADD TO CART")
    print("2.REMOVE FROM CART")
    print("3.UPDATE CART")
    print("4.BILL")
    print("5.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        print("------ITEMS IN THE SHOP------")
        select="select * from grocery"
        cur.execute(select)
        shop=cur.fetchall()
        for i in range(len(shop)):
            print(shop[i][1])
        for i in range(int(input("Enter the no of items you want\n"))):
            name=input("Enter the name of the item you want\n")
            quantity=int(input("Enter the no of quantity you want\n"))
            add(name,quantity)
    elif(choice==2):
        name=input("Enter the name of the item\n")
        remove(name)
    elif(choice==3):
        name=input("Enter the name of the item\n")
        quantity=int(input("Enter the quantity\n"))
        update(name,quantity)
    elif(choice==4):
        cnt=bill()
        print("Total bill is",cnt)
    elif(choice==5):
        print("EXITED")
        break
db.close()
