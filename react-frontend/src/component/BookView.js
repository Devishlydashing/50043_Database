import React from 'react'
import { Card,Image,Icon } from 'semantic-ui-react'

const BookView = ({book}) => (
    <div>
      <Card>
      <Image src={book.imUrl} wrapped ui={false} />
      <Card.Content>
<Card.Header>{book.asin}</Card.Header>
        <Card.Meta>
  <span className='date'>$ {book.price}</span>
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
      </Card>
    </div>
)
export default BookView