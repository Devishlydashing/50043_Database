from flask import jsonify
from flask_restful import Resource, reqparse
from books.model import Reviews

class Review(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('asin',
        type=vars,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('reviewText',
        type=vars,
        required=False,
        help="Every review needs a reviewText"
    )
    parser.add_argument('reviewerID',
        type=vars,
        required=False,
        help="Every review needs a reviewerID"
    )
    parser.add_argument('reviewerName',
        type=vars,
        required=False,
        help="Every review needs a reviewerName"
    )
    parser.add_argument('summary',
        type=vars,
        required=False,
        help="Every review needs a summary"
    )

    # Get a review based on id
    def get(self, id):
        review = Reviews.find_by_id(id)
        if not review:
            return {'message': f'There is no review with id {id}'}
        return jsonify(review.json())
        
    # Add a new review
    def post(self):
        data = Review.parser.parse_args()
        print(data)
        review = Reviews(**data)

        try:
            review.save_to_db()
        except:
            return {'message': 'An error occurred when inserting review'}, 500
        
        return review.json(), 201

    # Delete a review based on id
    def delete(self, id):
        review = Reviews.find_by_id(id)
        if not review:
            return {'message': f'There is no review with id {id}'}
        else:
            review.delete_from_db()
            return {'message': f'Review of {id} deleted'}

class ReviewList(Resource):

    # Get all the reviews based on asin
    def get(self, asin):
        review_list = Reviews.find_by_asin(asin)
        if not review_list:
            return {'message': f'There are no reviews with asin {asin}'}
        
        result = [review.json() for review in review_list]
        return jsonify(result)

    # Delete all reviews based on asin
    def delete(self, asin):
        review_list = Reviews.find_by_asin(asin)
        if not review_list:
            return {'message': f'There are no reviews with asin {asin}'}

        for review in review_list:
            review.delete_from_db()
        return {'deleted': True}
