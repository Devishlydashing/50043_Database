import React from 'react';
import FixedMenuLayout from "./FixedMenuLayout";
import Mygrid from "./BottomNav";
import './App.css';
import axios from 'axios';
import BookView from './component/BookView';
import { Container, Pagination } from 'semantic-ui-react';
import { useHistory } from "react-router-dom";

const { MONGO_IP } = process.env;

class ResultPage extends React.Component{
  constructor(props){
      super(props)
      this.state = {
        //   theSearch : 
        //   theOption : this.props.userOption
        books: [],
        theSearch : this.props.location.state.userSearch,
        theOption : this.props.location.state.userOption
      }
  }

  componentDidMount(){
    console.log(this.state.theSearch);
    console.log(this.state.theOption);
    if (this.state.theOption=='title'){
        console.log("hit")
        axios.get("http://"+ { MONGO_IP }+"/bookSearch?title="+this.state.theSearch)
        .then(res => {
            const books = [res.data];
            if (books==[]){
              alert("No matching books found")
            }
            //this.setState({ books });
            else{
              console.log(books);
              this.setState({ books });
            }   
            })    
    }  
    if (this.state.theOption=='author'){
        axios.get("http://"+ { MONGO_IP } +"/bookSearch?author="+this.state.theSearch)
        .then(res => {
            console.log(res)
            const books = res.data;
            if (books==""){
              alert("No matching books found")
            }
            this.setState({ books });
            console.log(books)
            })
      }
}
  renderBooks() {
    return (
        this.state.books.map(book=> {
        return <div class="four wide column" ><BookView key={book.asin} book={book}></BookView></div>
        })
    )
    }
  render(){
    const { books,activePage } = this.state
    return (
    <div>
      <FixedMenuLayout />
      <Container>       
        {/* <Myheader books={books}/>  */}
        <div class="ui grid" style={{ marginTop: '2em' }}>
          {this.renderBooks()}
        </div>
      </Container>  
      <Mygrid />
   </div>
    );
  }
  
}

export default ResultPage;