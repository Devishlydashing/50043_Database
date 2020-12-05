import React,{useState} from 'react';
import { Button, Container, Form,TextArea } from 'semantic-ui-react';
import FixedMenuLayout from "./FixedMenuLayout";
import axios from 'axios';

const { MONGO_IP } = process.env;

const AddBook = () => {
    const [asin, setAsin] = useState('');
    const [price, setPrice] = useState('');
    const [imURL, setImURL] = useState('');
    const [categories, setCategories] = useState('');
    const [description, setDescription] = useState('');

    const asinHandler = e => {
        setAsin(e.target.value);
    };
    const priceHandler = e => {
        setPrice(e.target.value);
    };
    const imURLHandler = e => {
        setImURL(e.target.value);
    };
    const categoriesHandler = e => {
        setCategories(e.target.value);
    };
    const descriptionHandler = e => {
        setDescription(e.target.value);
    };
    const submitHandler = e => {
        if (asin=='' || price=='' || imURL=='' || categories=='' || description ==''){
            alert("Please fill in all required fields");
        }
        else{
        const submitURL = 'http://'+ { MONGO_IP } +'/bookPost'
        e.preventDefault();
        console.log({asin,price,imURL,categories,description});
        axios.post(submitURL,{asin,price,imURL,categories,description})
        .then(res => {
            console.log(res)
            if (res.status===201){
                alert('Book Submitted Successfully')
            }
            if (res.status===404){
                alert('Add Book Failed - Book Already Exist')
            }
        })
    }
    };

    return(
        <div style={{ paddingTop: '50px' }}>
            <Container>  
            <FixedMenuLayout />
                <Form onSubmit={submitHandler}>
                    <Form.Field required>
                    <label>Asin</label>
                    <input placeholder='ISBN' onChange={asinHandler}/>
                    </Form.Field>
                    <Form.Field required> 
                    <label>Price</label>
                    <input placeholder='Price of book' onChange={priceHandler} />
                    </Form.Field>
                    <Form.Field required>
                    <label>imURL</label>
                    <input placeholder='Url to the book cover' onChange={imURLHandler} />
                    </Form.Field>
                    <Form.Field required>
                    <label>Categories</label>
                    <input placeholder='Categories' onChange={categoriesHandler}/>
                    </Form.Field>
                    
                    <Form.Field
                    // required
                    control={TextArea}
                    label='Description'
                    placeholder='Tell us more about the book...'
                    onChange={descriptionHandler}
                    />
                    <Button type='submit'>Submit</Button>
                </Form> 
            </Container>  
        </div>   
    )
    }
export default AddBook;