# Write a program to accept ID, fetch the document from collection, copy it in another collection "outofstock" and delete the document from the "mobiles" collection 
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["shoppings"]
coll=db["mobiles"]

qr={}
id=int(input('enter id to delete: '))
qr["_id"]=id

print(qr)
coll.delete_one(qr)
print('document deleted...')