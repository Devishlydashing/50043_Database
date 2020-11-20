import React from 'react';
import logo from './logo.svg';
import FixedMenuLayout from "./FixedMenuLayout";
import Myheader from "./MainGrid";
import Mygrid from "./BottomNav";
import './App.css';
import axios from 'axios';
import BookView from './component/BookView';
import { Pagination } from 'semantic-ui-react';

class App extends React.Component{
  state = {
    books: [],
    activePage: 5,
    apiUrl : 'https://cors-anywhere.herokuapp.com/http://ec2-54-90-244-6.compute-1.amazonaws.com/allbooks?page='
  };

  handlePaginationChange = (e, { activePage }) => {
    //console.log("page changed",{activePage});
    this.setState({ activePage });
    axios.get(this.state.apiUrl+this.state.activePage*8)
    .then(res => {
      const books = res.data;
      console.log(books)
      this.setState({ books });
      return (
        this.state.books.map(book=> {
          return <div class="four wide column" style={{ marginTop: '4em' }}><BookView key={book.asin} book={book}></BookView></div>
        })
      )
      })

  }
  componentDidMount() {
    axios.get(this.state.apiUrl+this.state.activePage)
    .then(res => {
      const books = res.data;
      console.log(books)
      this.setState({ books });
      })
  }
  renderBooks() {
    return (
      this.state.books.map(book=> {
        return <div class="four wide column" style={{ marginTop: '4em' }}><BookView key={book.asin} book={book}></BookView></div>
      })
    )
  }
  render(){
    const { books,activePage } = this.state
    return (
      <div>
      <FixedMenuLayout />
      {/* <Myheader books={books}/>  */}
      <div class="ui grid">
        {this.renderBooks()}
      </div>
      <Pagination
            onPageChange={this.handlePaginationChange}
            activePage={activePage}
            totalPages={100}
      />      
      <Mygrid />
   </div>
    );
  }
  
}

export default App;
