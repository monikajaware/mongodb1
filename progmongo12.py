# Write a program to accept price and display all documents having price less than the input value 
from ast import LtE
from sqlite3 import Cursor
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["shoppings"]
coll=db["mobiles"]

ch={}
pri=int(input('price: '))
ch["price"]=pri

filter={"price":pri}
Cursor=coll.find(filter)
