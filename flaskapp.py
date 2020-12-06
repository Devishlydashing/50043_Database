from flask import Flask
from flask_restful import Api
from db import db
from books.resource import Review, ReviewList
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/50043_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This turns off FlaskSQLAlchemy modification tracker but not SQLAlchemy modification tracker
db.init_app(app)
api = Api(app)

api.add_resource(Review, '/review/')
api.add_resource(ReviewList, '/reviews/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
