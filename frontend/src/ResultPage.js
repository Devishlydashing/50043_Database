import React from 'react';
import FixedMenuLayout from "./FixedMenuLayout";
import Mygrid from "./BottomNav";
import './App.css';
import axios from 'axios';
import BookView from './component/BookView';
import { Container, Pagination } from 'semantic-ui-react';

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

  updateBooks(){
    if (this.state.theOption=='title'){
      console.log("hit")
      console.log("http://"+ process.env.REACT_APP_MONGO_IP+"/bookSearch?title="+this.state.theSearch)
      axios.get("http://"+ process.env.REACT_APP_MONGO_IP+"/bookSearch?title="+this.state.theSearch)
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
      axios.get("http://"+ process.env.REACT_APP_MONGO_IP +"/bookSearch?author="+this.state.theSearch)
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

  componentDidMount(){
    console.log(this.state.theSearch);
    console.log(this.state.theOption);
    this.updateBooks();
    
}
  renderBooks() {
    return (
        this.state.books.map(book=> {
        return <div class="four wide column" ><BookView key={book.asin} book={book}></BookView></div>
        })
    )
    }
  
  onSubmit = (searchTerm,searchOption) => {
    console.log('from resultpage', searchTerm,searchOption);

    this.setState({theSearch:searchTerm,theOption:searchOption})
    this.updateBooks();
    // this.setState(theSearch)
  }

  render(){
    const { books,activePage } = this.state
    return (
    <div>
      <FixedMenuLayout onSearchSubmit={this.onSubmit} />
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