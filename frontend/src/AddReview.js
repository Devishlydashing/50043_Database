import React,{useState} from 'react';
import { Button, Container, Form ,Rating} from 'semantic-ui-react';
import FixedMenuLayout from "./FixedMenuLayout";
import axios from 'axios';

const AddReview = () => {
    const [asin, setAsin] = useState('');
    const [reviewerID, setReviewerid] = useState('');
    const [reviewerName, setReviewername] = useState('');
    const [overall, setOverall] = useState('');
    const [reviewText, setReviewtext] = useState('');
    const [reviewTime, setReviewtime] = useState('');
    const [summary, setSummary] = useState('');

    const asinHandler = e => {
        setAsin(e.target.value);
    };
    const reviewerIDHandler = e => {
        setReviewerid(e.target.value);
    };
    const reviewerNameHandler = e => {
        setReviewername(e.target.value);
    }

    const overallHandler = (e,{ rating }) => {
        setOverall(rating);
    };
    const reviewTextHandler = e => {
        setReviewtext(e.target.value);
    };
    const reviewTimeHandler = e => {
        setReviewtime(e.target.value);
    };
    const summaryHandler = e => {
        setSummary(e.target.value);
    };
    const submitHandler = e => {
        e.preventDefault();
        if (asin=='' || reviewerID=='' || reviewerName=='' || overall=='' || reviewText=='' || reviewTime=='' || summary==''){
            alert("Please fill in all required fields");
        }
        else{
        //console.log({asin,overall,reviewText,reviewTime,summary});
        const params = {asin,reviewerID,reviewerName,overall,reviewText,reviewTime,summary}
        const data = Object.keys(params)
        .map(key => `${key}=${params[key]}`)
        .join('&');
        console.log(data)
        const submitURL = `http://`+process.env.REACT_APP_MYSQL_IP+`/review/?${data}`
        axios.post(submitURL,data)
        .then(res => {
            console.log(res);
            if (res.status===201){
                alert('Review Submitted Successfully')
            }
            if (res.status===400){
                alert('Add Review Failed - Review Already Exist')
            }
        })
    }
    };
    
    return(
        <div>
            <div>
            <FixedMenuLayout></ FixedMenuLayout>
            </div>
            <div style={{ paddingTop: '50px' }}>
            <Container>
            <Form onSubmit={submitHandler}>
                <Form.Field required>
                <label>Asin</label>
                <input placeholder='Asin' onChange={asinHandler}/>
                </Form.Field>
                <Form.Field required>
                <label>ID</label>
                <input placeholder='your ID' onChange={reviewerIDHandler}/>
                </Form.Field>
                <Form.Field required>
                <label>Name</label>
                <input placeholder='your name' onChange={reviewerNameHandler}/>
                </Form.Field>
                <Form.Field required>
                <label>Rating</label>
                <Rating icon='star' defaultRating={3} maxRating={5} onRate={overallHandler} />
                </Form.Field>
                <Form.TextArea label='Description' placeholder='Tell us more about the book...' onChange={reviewTextHandler} />
                <Form.Field required>
                <label>Time</label>
                <input placeholder='What time is it?' onChange={reviewTimeHandler}/>
                </Form.Field>
                <Form.Field required>
                <label>Summary</label>
                <input placeholder='How was the book in one line?' onChange={summaryHandler}/>
                </Form.Field>
                <Button type='submit'>Submit</Button>
            </Form>
            </Container>
            </div>   
        </div> 
    )
}
export default AddReview;