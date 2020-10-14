from flask import Flask,request,jsonify
from flask_mongoengine import MongoEngine
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'MetaData',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class Meta(db.Document):
    asin = db.IntegerField()
    title = db.StringField()
    price = db.IntegerField()
    imURL = db.URLField()
    also_bought = db.ListField(db.StringField())
    also_viewed = db.ListField(db.StringField())
    bought_together = db.ListField(db.StringField())
    salesrank = db.DictField()
    brand = db.StringField()
    category = db.ListField(db.StringField())

    def to_json(self):
        return {"asin": self.asin,
                "title": self.title,
                "price": self.price,
                "imURL": self.imURL,
                "also_bought": self.also_bought,
                "also_viewed": self.also_viewed,
                "bought_together": self.bought_together,
                "salesrank": self.salesrank,
                "brand": self.brand,
                "category": self.category}
    
@app.route('/', methods=['GET'])
def query_meta():
    asin = request.args.get('asin')
    meta = Meta.objects(asin=asin).first()
    if not meta:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(meta.to_json())

@app.route('/', methods=['PUT'])
def create_meta():
    request_info = json.loads(request.data)
    meta = Meta(asin=request_info['asin'],
                title=request_info['title'],
                price=request_info['price'],
                imURL=request_info['imURL'],
                also_bought=request_info['also_bought'],
                also_viewed=request_info['also_viewed'],
                bought_together=request_info['bought_together'],
                salesrank=request_info['salesrank'],
                brand=request_info['brand'],
                category=request_info['category'])
    meta.save()
    return jsonify(meta.to_json())

@app.route('/', methods=['POST'])
def update_meta():
    request_info = json.loads(request.data)
    meta = Meta.objects(asin=record['asin']).first()
    if not meta:
        return jsonify({'error': 'data not found'})
    else:
        meta.update(title=request_info['title'],
                price=request_info['price'],
                imURL=request_info['imURL'],
                also_bought=request_info['also_bought'],
                also_viewed=request_info['also_viewed'],
                bought_together=request_info['bought_together'],
                salesrank=request_info['salesrank'],
                brand=request_info['brand'],
                category=request_info['category'])
    return jsonify(meta.to_json())

@app.route('/', methods=['DELETE'])
def delete_record():
    request_info = json.loads(request.data)
    meta = Meta.objects(asin=request_info['asin']).first()
    if not meta:
        return jsonify({'error': 'data not found'})
    else:
        meta.delete()
    return jsonify(meta.to_json())

if __name__ == "__main__":
    app.run(debug=True)