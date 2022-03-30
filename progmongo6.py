# Write a program to show list of all documents from the collection
from pymongo import MongoClient

try: 
    client=MongoClient("mongodb://localhost:27017/")
    db=client["shoppings"]
    coll=db["mobiles"]


    for doc in coll.find():
        print(doc)
except:
    print('connection failed')