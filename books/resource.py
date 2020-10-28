from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from model import ReviewsModel

class Review(Resouce):
    parser = reqparse.RequestParser()
    parser.add_argument('asin',
        type=vars,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('reviewText',
        type=vars,
        required=True,
        help="Every review needs a reviewText"
    )
    parser.add_argument('reviewerID',
        type=vars,
        required=True,
        help="Every review needs a reviewerID"
    )
    parser.add_argument('reviewerName',
        type=vars,
        required=True,
        help="Every review needs a reviewerName"
    )
    parser.add_argument('summary',
        type=vars,
        required=True,
        help="Every review needs a summary"
    )

    # Add a new review
    def post(self, name):
        data = Review.parser.parse_args()
        review = ReviewsModel(**data)

        try:
            review.save_to_db()
        except:
            return {'message': 'An error occurred when inserting review'}, 500
        
        return review.json(), 201


class ReviewList(resource):

    def get(self, asin):
        reviews = ReviewsModel.find_by_asin(asin)
        return reviews