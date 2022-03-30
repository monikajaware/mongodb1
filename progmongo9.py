# Write a program to accept ID and new price of the mobile. Update the document with new price. Display the document after updating. 
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["shoppings"]
coll=db["mobiles"]

qr={}
id=int(input('enter id: '))
qr["_id"]=id
 
ch={}
pri=int(input('new price: '))
ch["price"]=pri

print(qr)
print(ch)

upd={"$set":ch}
coll.update_one(qr,upd)
print('document updated....')

for doc in coll.find(qr):
    print(doc)
        