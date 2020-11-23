import pymongo  # ORM
from pymongo import MongoClient
from bson.json_util import dumps,RELAXED_JSON_OPTIONS
import json
from flask_api import status
import time
from flask import Flask, session, request, jsonify, g
from utils import add_log # import adding logs function from utils.py
import pprint

app = Flask(__name__)

mongo_uri = "mongodb://localhost:27017/"
client = pymongo.MongoClient(mongo_uri)

# currently tested on localhost -- CHANGE database & collection names for EC2

# Get metadata of a book
# asin -- make sure not in form of a string
@app.route('/metadata/<asin>', methods=['GET'])
def query_meta(asin):
    db = client['MetaData'] # change to meta from MetaData for EC2 
    collection = db['metadata'] # change to newmetadata from metadata for EC2
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
    data = request.json
    db = client['MetaData']
    collection = db['metadata']
    collection1 = db['logs'] # Collection for logs -- create one in EC2 instance if haven't

    title = request.form.get("title")
    price = request.form.get("price")
    category = request.form.get("category")

    v = collection.find_one({"asin": data["asin"]})
    try:
        if data["asin"] == v["asin"]:
            response_code = 404
            add_log(request.method, request.url,{"book_information": {"title": title, "price": price, "category": category}}, response_code, collection1)   
            return {'message': 'Book exists. Please select another one!', 'data': {}}, 404
    except:
        # add into metadata collection
        post_id = collection.insert_one(data) 
        response_code = 201
        # add into logs collection
        add_log(request.method, request.url,{"book_information": {"title": title, "price": price, "category": category}}, response_code, collection1)    
        return {'message': 'Book added', 'data': str(post_id)}, 201


# searching for a book by title
@app.route('/bookSearch', methods=["POST"])
def search_books():
    data = request.json
    
    db = client['MetaData']
    collection = db['metadata']
    collection1 = db['logs']

    keyword = request.form.get("keyword")

    v = collection.find_one({"title": data["title"]})
    try:
        if data["title"] == v["title"]:
            response_code = 201
            add_log(request.method, request.url, {"search_keyword": keyword}, response_code, collection1)
            return {'message': 'Book exists.', 'data': str(v)}, 201
    except:
        response_code = 404
        add_log(request.method, request.url, {"search_keyword": keyword}, response_code, collection1)   
        return {'message': 'Book does not exist', 'data': {}}, 404
    
# Deleting a book
@app.route('/metadelete/<asin>', methods=['DELETE'])
def delete_record(asin):
    db = client['MetaData']
    collection = db['metadata']
    collection1 = db['logs']

    data = request.json
    v = collection.find_one({"asin": asin})
    try:
        if asin == v["asin"]:
            collection.remove({"asin": asin})
            response_code = 201
            add_log(request.method, request.url,{"book deleted": str(v)}, response_code, collection1)
            return {'message': 'Deleted metadata of book', 'data': str(v)}, 201
    except:
        response_code = 404
        add_log(request.method, request.url, {"book does not exist so not deleted"}, response_code, collection1)   
        return {'message': 'Book does not exist so cannot delete metadata', 'data': {}}, 404

# -- FIX THIS
# Adding a review
@app.route("/book/<asin>", methods=["POST"])
def review(asin):
    db = client['MetaData']
    collection1 = db['logs']

    rating = request.form.get("rating")
    title = request.form.get("title")
    comment = request.form.get("comment")
    
    response_code = 201
    add_log(request.method, request.url, {"title": title,  "comment": comment, "rating": rating}, response_code, collection1)
    v = collection1.find_one({"comment": comment}) # checks if comment has been written to log database
    return {'message': 'Added review logs', 'data': str(v)}, 201

# Delete a review
@app.route('/reviewdelete/<asin>', methods=['DELETE'])
def delete_review(asin):
    db = client['MetaData']
    collection1 = db['logs']

    data = request.json
    try:
        if asin == v["asin"]:
            response_code = 201
            add_log(request.method, request.url,{"book deleted": str(v)}, response_code, collection1)
            return {'message': 'Deleted review of book', 'data': str(v)}, 201
    except:
        response_code = 404
        add_log(request.method, request.url,{"book does not exist so cannot delete review"}, response_code, collection1)
        return {'message': 'Book does not exist so cannot delete review', 'data': {}}, 404

if __name__ == "__main__":
    app.run(debug=True)
