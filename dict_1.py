d={"a":1,2:"b","c":3,"d":4,5:"e"}
print(d["a"])

#-------Fetch-------

data=d[2]
print(data)
#-----to fetch value give key to the dictionary---------
d[key]
print(d["a"])
#-------Store---------

d["a"]=34
print(d["a"])

#------Remove-------

d.pop(5)
print(d)

#-----To print all keys------

keys=d.keys()
#-----dictionary printing in list format
keys=list(d.keys())
#----------------------------------
print(keys)

#-----To print all values------

values=d.values()
#-----dictionary printing in list format
values=list(d.values())
#-------------------------------------
print(values)


#-------dictionary in proper format-----
items=d.items()
#-----dictionary printing in list format
items=list(d.items())
#-------------------------------------

print(itmes)
