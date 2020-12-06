import pymongo
mongo_uri = "mongodb://localhost:27017/"
client = pymongo.MongoClient(mongo_uri)
db = client['meta']
collection= db['newmetadata']
collection.create_index([('title', 'text')], default_language='english')