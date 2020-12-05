import React from 'react'
import axios from 'axios';
import ReviewView from './component/ReviewView';
import { Comment,Container,Header } from 'semantic-ui-react';
import FixedMenuLayout from "./FixedMenuLayout";

class ReviewPage extends React.Component{
    state = {
        reviews : [],
        apiUrl : 'http://'+ process.env.REACT_APP_MYSQL_IP +'/reviews/?asin='
      };

    renderReviews() {
    return (
        this.state.reviews.map(review=> {
        return <div class="four wide column" style={{ marginTop: '2em' }}><ReviewView key={review.id} review={review}></ReviewView></div>
        })
    )
    }
    render(){
        const asin = this.props.match.params.asin;
        console.log(this.state.apiUrl+asin);
        axios.get(this.state.apiUrl+asin)
            .then(res => {
                console.log(res.status)
                if (res.status == 404){
                    alert("No book reviews available")
                }
                const reviews = res.data;
                this.setState({ reviews });
            })
        return(
            <div>
                <FixedMenuLayout />
                <div style={{ paddingTop: '50px' }}>
                <Container>
                <Comment.Group>
                    <Header as='h3' dividing>
                        Book Reviews
                    </Header>    
                    <div>
                        {this.renderReviews()}
                    </div>
                </Comment.Group>
                </Container>
                </div>
            </div>
        )
    }
    }

export default ReviewPage