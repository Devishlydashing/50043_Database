from flask import jsonify, request
from flask_restful import Resource, reqparse
from books.model import Reviews

class Review(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('asin',
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('reviewText',
        required=True,
        help="Every review needs a reviewText"
    )
    parser.add_argument('reviewerID',
        required=True,
        help="Every review needs a reviewerID"
    )
    parser.add_argument('reviewerName',
        required=True,
        help="Every review needs a reviewerName"
    )
    parser.add_argument('summary',
        required=True,
        help="Every review needs a summary"
    )

    # Get a review based on id
    def get(self):
        id_val = request.args.get('id')
        review_list = Reviews.find_by_id(id_val) # returns a list

        if not review_list:
            return {'message': f'There is no review with id {id_val}'}, 404
        review = review_list[0]
        return jsonify(review.json())
        
    # Add a new review
    def post(self):
        data = Review.parser.parse_args()
        review = Reviews(**data)

        try:
            review.save_to_db()
        except:
            return {'message': 'An error occurred when inserting review'}, 500
        
        return review.json(), 201

    # Delete a review based on id
    def delete(self):
        id_val = request.args.get('id')
        review_list = Reviews.find_by_id(id_val)
        
        if not review_list:
            return {'message': f'There is no review with id {id_val}'}, 404
        else:
            review = review_list[0]
            review.delete_from_db()
            return {'message': f'Review of id {id_val} deleted'}

class ReviewList(Resource):

    # Get all the reviews based on asin
    def get(self):
        asin_val = request.args.get('asin')
        review_list = Reviews.find_by_asin(asin_val)
        if not review_list:
            return {'message': f'There are no reviews with asin {asin_val}'}, 404
        
        result = [review.json() for review in review_list]
        return jsonify(result)

    # Delete all reviews based on asin
    def delete(self):
        asin_val = request.args.get('asin')
        review_list = Reviews.find_by_asin(asin_val)
        if not review_list:
            return {'message': f'There are no reviews with asin {asin_val}'}, 404

        for review in review_list:
            review.delete_from_db()
        return {'message': f'Review of asin {asin_val} deleted'}
