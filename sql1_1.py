import pymysql as con
db=con.connect(
    host="localhost",
    user="root",
    password="root",
    database="student")
print("successfull connected")
cur=db.cursor()
#--------insert query------------
'''insert="insert into classa values(%s,%s,%s)"
value=[0,"abc",23]
cur.execute(insert,value)
db.commit()
print("added successfully")'''
#--------select query-------------
select="select * from classa"
cur.execute(select)
data=cur.fetchall()
print("FULL DATA IN THE DATABASE\n",data)
#--------select where query--------
select="select * from classa where name=%s"
value=["zaid"]
cur.execute(select,value)
data=cur.fetchone()
print("\n\n",value,"\n",data)
#--------Update query--------------
update="update classa set name=%s where idclassa=%s"
value=["pranav",1]
cur.execute(update,value)
db.commit()
print("\nUpdated successfully")
#--------Delete query
delete="delete from classa where idclassa=%s"
value=[1]
cur.execute(delete,value)
db.commit()
print("\ndeleted successfully")
db.close()
