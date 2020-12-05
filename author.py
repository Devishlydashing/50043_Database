import pymongo  # ORM
from pymongo import MongoClient
from bson.json_util import dumps,RELAXED_JSON_OPTIONS
import json
import time
from flask import Flask, session, request, jsonify, g
from utils import add_log # import adding logs function from utils.py

app = Flask(__name__)

mongo_uri = "mongodb://localhost:27017/"
client = pymongo.MongoClient(mongo_uri)

# Get all books
@app.route('/allbooks',methods=["GET"])
def get_allbooks_paginated():
    db = client['meta']
    col= db['newmetadata']
    page = request.args.get('page')
    if page == None:
        page = 2
    page = int(page)
    response = col.find().skip(page).limit(8)
    #return {'message':"found","books":str(list(response))},201
    return dumps(response)


# Get one book
# asin -- make sure not in form of a string
@app.route('/metadata/<asin>', methods=['GET'])
def query_meta(asin):
    db = client['meta'] # change to meta from MetaData for EC2
    collection = db['newmetadata'] # change to newmetadata from metadata for EC2
    v = collection.find_one({"asin": asin})
    try:
        if asin == v["asin"]:
            # returns the metadata for particular book
            return {'message': "Book's metadata exists", 'data': str(v)}, 201
    except:
        return {'message': "Book's metadata does not exists", 'data': {}}, 404

# Add a new book -- needs everything from frontend (asin & title & price & category)
@app.route('/bookPost', methods=["POST"])
def post_books():
    asin = request.args.get('asin')
    title = request.args.get('title')
    price = request.args.get('price')
    category = request.args.get('category')

    db = client['meta']
    collection = db['newmetadata']
    collection1 = db['logs'] # Collection for logs -- create one in EC2 instance

    v = collection.find_one({"asin": asin})
    try:
        if asin == v["asin"]:
            response_code = 404
            add_log(request.method, request.url,{"book_information": {"title": title, "price": price, "category": category}}, response_code, collection1)    
            return {'message': 'Book exists. Please select another one!', 'data': {}}, 404
    except:
        # add into metadata collection
        post_id = collection.insert_one(request.args.to_dict())
        vv = collection.find_one({"asin": asin})
        response_code = 201
        # add into logs collection
        add_log(request.method, request.url,{"book_information": {"title": title, "price": price, "category": category}}, response_code, collection1) 
        return {'message': 'Book added', 'data': str(vv)}, 201

# searches for a book - need page & EITHER title OR author OR category
@app.route('/bookSearch', methods=["GET"])
def search_books():
    page = request.args.get('page')
    if page == None:
        page = 2
    page = int(page)

    db = client['meta']
    collection = db['newmetadata']
    collection1 = db['logs']
    if(request.args.get("title") != None):
        mytitle = request.args.get("title")
        v = collection.find_one({"title":{'$regex': mytitle, '$options': 'i'}})
        if v != None:
            response_code=201
            add_log(request.method, request.url,{"book_information": {"title searched": request.args.get("title")}}, response_code, collection1)
            return dumps(v)
        else:     
            response_code=404
            add_log(request.method, request.url,{"book_information": {"title searched": request.args.get("title")}}, response_code, collection1)
            return {'message': 'Book does not exists!', 'data': {}}, 404
    if(request.args.get("author") != None):
        myauthor = request.args.get("author")
        v = collection.find({"author":{'$regex': myauthor, '$options': 'i'}}) # add .skip(page).limit(8)
        if v != None:
            response_code=201
            add_log(request.method, request.url,{"book_information": {"author searched": request.args.get("title")}}, response_code, collection1)
            return dumps(v)
        else:     
            response_code=404
            add_log(request.method, request.url,{"book_information": {"author searched": request.args.get("title")}}, response_code, collection1)
            return {'message': 'Book does not exists!', 'data': {}}, 404
    if(request.args.get("category") != None):
        v = collection.find({"categories": {"$elemMatch":{"$elemMatch":{"$in":[request.args.get("category")]}}}}).skip(page).limit(8)
        if(v.count() == 0):
            response_code=404
            add_log(request.method, request.url,{"book_information": {"category searched": request.args.get("category")}}, response_code, collection1)
            return {'message': 'Book does not exists!', 'data': {}}, 404
        if(v != None):
            response_code=201
            add_log(request.method, request.url,{"book_information": {"category searched": request.args.get("category")}}, response_code, collection1)
            return dumps(v)
    else:
        return {'message': "Error"}, 404

# Deleting a book -- need asin
@app.route('/metadelete', methods=['DELETE'])
def delete_record():
    db = client['meta']
    collection= db['newmetadata']
    collection1 = db['logs']

    asin1 = request.args.get('asin')
    v = collection.find_one({"asin": asin1})
    try:
        if asin1 == v["asin"]:
            collection.remove({"asin": asin1})
            response_code = 201
            add_log(request.method, request.url,{"book deleted": str(v)}, response_code, collection1)
            return {'message': 'Deleted metadata of book', 'data': str(v)}, 201
    except:
        response_code = 404
        add_log(request.method, request.url, {"book does not exist so not deleted": asin1}, response_code, collection1)
        return {'message': 'Book does not exist so cannot delete metadata', 'data': {}}, 404

#make searchbar dynamic
@app.route('/dynamicSearch',methods=["GET"])
def dynamic_search():
    db = client['meta']
    collection= db['newmetadata']
    search_query = request.args.get('author')
    res = collection.find({"$text": {"$search": search_query}})
    if res != None:
            response_code=201
            return dumps(res)
    else:
        return {'message': 'Book does not exists!', 'data': {}}, 404



if __name__ == "__main__":
    app.run()
