import React from 'react'
import { Comment, Rating} from 'semantic-ui-react';

class ReviewView extends React.Component{
    render(){
        return(
            <div>
            <Comment>
                <Comment.Content>
                    <Comment.Author as='a'>{this.props.review.reviewerName}</Comment.Author>
                
                    <Comment.Metadata>
                        {this.props.review.reviewTime}
                    </Comment.Metadata>
                    <Comment.Metadata>
                        <Rating defaultRating={this.props.review.overall} maxRating={5} disabled />
                    </Comment.Metadata>
                    <Comment.Text>{this.props.review.reviewText}</Comment.Text>
                </Comment.Content>
            </Comment>
            </div>

        )
    }
}
export default ReviewView;