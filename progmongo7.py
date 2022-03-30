# Write a program to take ID as input, search and display the document with mobile information

from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["shoppings"]
coll=db["mobiles"]

id=int(input('enter product id : '))
qr={}
qr["_id"]=id

for doc in coll.find(qr):
    print(doc)



