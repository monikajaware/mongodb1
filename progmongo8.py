# Write a program to take company as an input and display documents of all mobiles of the company 
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["shoppings"]
coll=db["mobiles"]

cmp=input("enter company: ")
d={}
d['company']=cmp

for doc in coll.find(d):
        print(doc)