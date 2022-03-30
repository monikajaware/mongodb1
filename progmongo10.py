# Write a program to accept ID, ram and rom. Update the document with new ram and rom of the model. (memory size – temp & permanent) 

from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["shoppings"]
coll=db["mobiles"]

qr={}
id=int(input('enter id: '))
qr["_id"]=id
 
ch={}
ram=input('Ram: ')
ch["Ram"]=ram

mh={}
rom=input('Rom: ')
mh["Rom"]=ram

print(qr)
print(ch)
print(mh)

upd={"$set":ch}
coll.update_one(qr,upd)
upd={"$set":mh}
coll.update_one(qr,upd)

print('document updated....')