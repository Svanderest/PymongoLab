from pymongo import MongoClient
from blogs import blog_docs
mongo_client = MongoClient("localhost", 27017)

db = mongo_client.lab4
coll = db.blogs
result = coll.insert_many(blog_docs)
print(result)

