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

# Add a new book
@app.route('/bookPost', methods=["POST"])
def post_books():
    asin = request.args.get('asin')

    db = client['meta']
    collection = db['newmetadata']
    collection1 = db['logs'] # Collection for logs -- create one in EC2 instanc$

    # title = request.form.get("title")
    # price = request.form.get("price")
    # category = request.form.get("category")

    v = collection.find_one({"asin": asin})
    try:
        if asin == v["asin"]:
            response_code = 404
            # add_log(request.method, request.url,{"book_information": {"title": title, "price": price, "category": category}}, response_code, collection1)   
            return {'message': 'Book exists. Please select another one!', 'data': {}}, 404
    except:
        # add into metadata collection
        post_id = collection.insert_one(request.args.to_dict())
        vv = collection.find_one({"asin": asin})
        response_code = 201
        # add into logs collection
        # add_log(request.method, request.url,{"book_information": {"title":  title, "price": price, "category": category}}, response_code, collection1)
        return {'message': 'Book added', 'data': str(vv)}, 201


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
        v = collection.find_one({"title":request.args.get("title")})
        response_code=201
        #add_log(request.method, request.url,{"book_information": {"title searched": request.args.get("title")}}, response_code, collection1)
        return str(v)
    if(request.args.get("author") != None):
        response_code=201
        #add_log(request.method, request.url,{"book_information": {"author searched": request.args.get("author")}}, response_code, collection1)
        v = collection.find({"author":request.args.get("author")}) # add .skip($
        return dumps(v)
    if(request.args.get("category") != None):
        v = collection.find({"categories": {"$elemMatch":{"$elemMatch":{"$in":[request.args.get("category")]}}}}).skip(page).limit(8)
        response_code=201
        #add_log(request.method, request.url,{"book_information": {"category searched": request.args.get("category")}}, response_code, collection1)
        return dumps(v)
    else:
        return {'message': "Error"}, 404

# Deleting a book
@app.route('/metadelete', methods=['DELETE'])
def delete_record():
    db = client['meta']
    collection = db['newmetadata']
    collection1 = db['logs']

    #data = request.json
    asin1 = request.args.get('asin')
    v = collection.find_one({"asin": asin1})
     try:
        if asin1 == v["asin"]:
            collection.remove({"asin": asin1})
            response_code = 201
            # add_log(request.method, request.url,{"book deleted": str(v)}, response_code, collection1)
            return {'message': 'Deleted metadata of book', 'data': str(v)}, 201
    except:
        response_code = 404
        # add_log(request.method, request.url, {"book does not exist so not deleted": str(v)}, response_code, collection1)
        return {'message': 'Book does not exist so cannot delete metadata', 'data': {}}, 404

if __name__ == "__main__":
    app.run(debug=True)
