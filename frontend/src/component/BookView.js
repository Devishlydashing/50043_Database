import React from 'react'
import { Card,Image,Icon,Button} from 'semantic-ui-react';
import { Link } from 'react-router-dom';

class BookView extends React.Component{
  nextPath(path) {
    this.props.history.push(path);
  }
  render(){
    return(
      <div> 
      {/* <Link to={book.asin}> */}
      <Card as={Link} to={this.props.book.asin} >
      {/* <Button as={Link} to={this.props.book.asin}> */}
      <Image src={this.props.book.imUrl} wrapped ui={false} />
      <Card.Content>
      <Card.Header>{this.props.book.title}</Card.Header>
        <Card.Meta>
        <span className='date'>{this.props.book.author}</span>
        </Card.Meta>
        {/* <Card.Description>
          {book.description}
        </Card.Description> */}
      </Card.Content>
      {/* <Card.Content extra>
        <a>
          <Icon name='user' />
          22 Friends
        </a>
      </Card.Content> */}
      {/* </Button> */}
      </Card>     
      {/* </Link> */}
    </div>
    )
  }
}
export default BookView