# Write a python program to take input from the user and add employee data as a document in the collection (ex. ID, company, model, processor, screensize, ram, rom, connectivity, price, rating, etc.) 
from pymongo import MongoClient


client=MongoClient("mongodb://localhost:27017")
db=client["shoppings"]
coll=db["mobiles"]

id=int(input('enter product id : '))
cmp=input('enter company : ')
mod=input('Model : ')
pro=input('processor : ')
scs=input('screen size : ')
rm=input('Ram: ')
ro=input('Rom : ')
co=input('connectivity : ')
pri=int(input('Price : '))
rat=int(input('rating: '))

dic={}
dic["_id"]=id
dic["company"]=cmp
dic["model"]=mod
dic["processor"]=pro
dic["screen size"]=scs
dic["Ram"]=rm
dic["Rom"]=ro
dic["connectivity"]=co
dic["price"]=pri
dic["rating"]=rat

coll.insert_one(dic)
print('new product added to mobile collection')




