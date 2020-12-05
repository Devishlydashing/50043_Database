import React from 'react';
import FixedMenuLayout from "./FixedMenuLayout";
import Mygrid from "./BottomNav";
import './App.css';
import axios from 'axios';
import BookView from './component/BookView';
import { Container, Pagination } from 'semantic-ui-react';


class HomePage extends React.Component{
  state = {
    books: [],
    activePage: 1,
    apiUrl : 'http://'+ process.env.REACT_APP_MONGO_IP+'/allbooks?page='
  };

  handlePaginationChange = (e, { activePage }) => {
    //console.log("page changed",{activePage});
    console.log(this.state.apiUrl)
    this.setState({ activePage });
    axios.get(this.state.apiUrl+this.state.activePage*8)
    .then(res => {
      const books = res.data;
      console.log(books)
      this.setState({ books });
      return (
        this.state.books.map(book=> {
          return <BookView key={book.asin} book={book}></BookView>
        })
      )
      })

  }
  componentDidMount() {
    axios.get(this.state.apiUrl+this.state.activePage)
    .then(res => {
      const books = res.data;
      this.setState({ books });
      
      })
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
        <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
        }}
        >
        <Pagination
              onPageChange={this.handlePaginationChange}
              activePage={activePage}
              totalPages={100}
              
        /> 
        </div>     
      </Container>  
      {/* <Mygrid /> */}
   </div>
    );
  }
  
}

export default HomePage;

