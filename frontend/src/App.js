import React from 'react';
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import AddReview from './AddReview';
import AddBook from './AddBook';
import HomePage from "./HomePage";
import ReviewPage from "./ReviewPage";
import ResultPage from './ResultPage';

class App extends React.Component{
  render(){
    return (
      <BrowserRouter>
        <Switch>
          {/* <Route exact path = "/" component={LoginForm}/> */}
          <Route exact path="/result" component={ResultPage} />
          <Route exact path="/home" component={HomePage} />
          <Route exact path="/addreview" component={AddReview} />
          <Route exact path="/addbook" component={AddBook} />
          <Route path="/:asin" component={ReviewPage} />
          
        </Switch>
      </BrowserRouter>
    );
  }  
}

export default App;
