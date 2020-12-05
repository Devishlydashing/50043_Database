from bson.json_util import dumps, RELAXED_JSON_OPTIONS
import json
import pymongo
import requests
from bs4 import BeautifulSoup

mongo_uri = "mongodb://localhost:27017/"
client = pymongo.MongoClient(mongo_uri)
db = client['MetaData']
collection = db['meta']


def get_author(query_string):
    # query_string = B000FC127I
    URL = "https://www.goodreads.com/search?q="
    page = requests.get(URL+query_string)

    soup = BeautifulSoup(page.content, 'html.parser')
    spans = soup.find_all("span", itemprop="name")
    if spans == []:
        return "na", "na"
    # imageURL = soup.find_all(class_="bookCover",itemprop="image")
    title = spans[0].text
    author = spans[1].text
    # url = imageURL[0]['src']
    return title, author


cursors = collection.find()
for cursor in cursors:
    # print(str(cursor['asin']))
    title, author = get_author(str(cursor['asin']))
    #print(title, author)
    collection.update({"asin": str(cursor['asin'])}, {
                      "$set": {'title': title, "author": author}})
    #print(collection.find_one({"asin": str(cursor['asin'])}))
# print(get_author("B000FC127I"))
