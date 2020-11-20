import React from 'react'
import {
  Container,
  Grid,
  Image,
} from 'semantic-ui-react';
import BookView from './component/BookView';

const MainGrid = () => (
<div>
 <Container text style={{ marginTop: '4em' }}>
  <Grid>
    <Grid.Row columns={4}>
      <Grid.Column>
        <BookView />
      </Grid.Column>
      <Grid.Column>
        <BookView />
      </Grid.Column>
      <Grid.Column>
        <BookView />
      </Grid.Column>
      <Grid.Column>
        <BookView />
      </Grid.Column>
    </Grid.Row>

    <Grid.Row columns={4}>
      <Grid.Column>
        <BookView />
      </Grid.Column>
      <Grid.Column>
        <BookView />
      </Grid.Column>
      <Grid.Column>
        <BookView />
      </Grid.Column>
      <Grid.Column>
        <BookView />
      </Grid.Column>
    </Grid.Row>
  </Grid>
</Container>
</div>
)

export default MainGrid