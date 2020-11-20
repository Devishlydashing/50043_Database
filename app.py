from flask import Flask
from flask_restful import Api
from db import db
from books.resource import Review, ReviewList

app = Flask(__name__)
db.init_app(app)

# replace localhost: ip_address (for ec2), db_name: database name
# DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='password', server='localhost', database='50043_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/50043_db' # DATABSE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This turns off FlaskSQLAlchemy modification tracker but not SQLAlchemy modification tracker
api = Api(app)

api.add_resource(Review, '/review/<id>')
api.add_resource(ReviewList, '/reviews/<string:asin>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)