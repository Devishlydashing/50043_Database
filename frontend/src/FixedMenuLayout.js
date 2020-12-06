import React, { useState } from 'react'
import {
  Container,
  Dropdown,
  Search, 
  Menu,
  Icon
} from 'semantic-ui-react';
import { Link, withRouter } from 'react-router-dom';
import { ReactDOM,render} from "react-dom";
import axios from 'axios';
import _ from "lodash";
import BookView from './component/BookView';
import ResultPage from './ResultPage';

class FixedMenuLayout extends React.Component {
   options = [
    { key: 'author', text: 'author', value: 'author' },
    { key: 'title', text: 'title', value: 'title' },
  ]
  state = {
    userSearch: '',
    userOption: 'author',
    books: []
  };
  // let [userSearch, setuserSearch] = useState('');
  // let [userOption, setuserOption] = this.state.author;
  
  handleChange = e =>{
    console.log("hit");
    // setuserSearch(e.target.value);
    this.setState({userSearch:e.target.value});
    // place dynamic search here!
    axios.get('http://'+ process.env.REACT_APP_MONGO_IP+'/bookSearch?author='+this.state.userSearch)
    .then(res => {
      this.setState({books:res.data});
      console.log(this.state.books);
      console.log('out')
      
    })
    .catch(err=>{
      console.log(err.code);
    }
      )
  }
  
   handleOptions = (e,data) =>{
    //console.log(data.value);
    this.setState({userOption:data.value});
  }
  
   handleSubmit = e => {
     if(this.props.onSearchSubmit) {
      console.log(this.state.userSearch,this.state.userOption);
      this.props.onSearchSubmit(this.state.userSearch,this.state.userOption);
      return;
     }
     console.log('global search');
     if(!this.props.onSearchSubmit) {
      console.log("Submit search");
      if(this.props.history.location.pathname=='/result'){
        console.log("inside result");
      }
      else{
      this.props.history.push({
        pathname: '/result',
        state: this.state
      });
      }
      e.preventDefault();
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
  return(
  <div>
    <Menu fixed='top' inverted>
      <Container>
        <Menu.Item as='a' header as={Link} to="/home">
          {/* <Image size='mini' src='./logo.png' style={{ marginRight: '1.5em' }} /> */}
          Explore
        </Menu.Item>
        

        <Dropdown item simple text='Actions'>
          <Dropdown.Menu>
            <Dropdown.Item as={Link} to="addbook">Add book</Dropdown.Item>
            <Dropdown.Item as={Link} to="addreview">Add review</Dropdown.Item>
            <Dropdown.Divider />
            <Dropdown.Header>Settings</Dropdown.Header>
            {/* <Dropdown.Item>
              <i className='dropdown icon' />
              <span className='text'>Profile</span>
              <Dropdown.Menu>
                <Dropdown.Item>Manage</Dropdown.Item>
                <Dropdown.Item>Delete</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown.Item> */}
            <Dropdown.Item>Log Out</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
        <Dropdown item simple text='Type' defaultValue='author' options={this.options} onChange={this.handleOptions}/>
        <Search
          labelPosition='left'
          placeholder='Search...'
          
          results = {this.state.books}
          icon={<Icon name='search' inverted circular link link onClick={this.handleSubmit}/>}
          onSearchChange={_.debounce(this.handleChange, 300)}
        />
      </Container>
    </Menu>
  </div>
  )
  }
}

export default  withRouter(FixedMenuLayout)