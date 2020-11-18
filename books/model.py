from db import db
from datetime import datetime

class ReviewsModel(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    asin = db.Column(db.VARCHAR(100))
    helpful = db.Column(db.VARCHAR(100))
    overall = db.Column(db.Integer)
    reviewText = db.Column(db.VARCHAR(255))
    reviewTime = db.Column(db.Date)
    reviewerID = db.Column(db.VARCHAR(100))
    reviewerName = db.Column(db.VARCHAR(100))
    summary = db.Column(db.VARCHAR(255))
    unixReviewTime = db.Column(db.Integer)

    # Initialize w critical information | Others initialize to 0 or respective timing
    def __init__(self, asin, reviewText, reviewerID, reviewerName, summary):
        self.asin = asin
        self.helpful = "[0, 0]"
        self.overall = 0
        self.reviewText = reviewText

        now = datetime.now()
        self.reviewTime = now.strftime("%Y-%-m-%-d")
        
        self.reviewerID = reviewerID
        self.reviewerName = reviewerName
        self.summary = summary
        self.unixReviewTime = int(now.timestamp())

    def json(self):
        return {
            'id': self.id,
            'asin': self.asin,
            'helpful': self.helpful,
            'overall': self.overall,
            'reviewText': self.reviewText,
            'reviewTime': self.reviewTime,
            'reviewerID': self.reviewerID,
            'reviewerName': self.reviewerName,
            'summary': self.summary,
            'unixReviewTime': self.unixReviewTime
        }

    @classmethod
    def find_by_asin(cls, asin):
        return cls.query.filter_by(asin=asin).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()