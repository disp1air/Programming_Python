import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

db = client.test
col = db.unicorns

db1 = client.test_shop
col1 = db1.users

pprint.pprint(col.find_one({"name": "Leia"}))
pprint.pprint(col1.find_one({"username": "User3"}))

# Insert a document
result = db.unicorns.insert_one({
    "name": "python_pi",
    "loves": ["banana", "Jameson"],
    "weight": 127,
    "gender": "m",
    "vampires": 123
})

result1 = db1.users.insert_one({
    "username" : "User7",
    "email" : "User7@mail.ru",
    "password" : "User7pass"
})

print(result)
print(result1)

# Delete a document
delete = db.unicorns.delete_one({"name" : "Pilot"})
delete1 = db1.users.delete_one({ "username" : "User7"})

print(delete)
print(delete1)