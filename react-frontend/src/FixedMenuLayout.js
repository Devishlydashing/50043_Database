import React, { Component } from 'react'
import {
  Container,
  Dropdown,
  Image,
  Menu,
} from 'semantic-ui-react';
import Mysearchbar from './component/Mysearchbar';

const FixedMenuLayout = () => (
  <div>
    <Menu fixed='top' inverted>
      <Container>
        <Menu.Item as='a' header>
          <Image size='mini' src='./logo.png' style={{ marginRight: '1.5em' }} />
          Home
        </Menu.Item>
        <Menu.Item as='a'>My Favorites</Menu.Item>

        <Dropdown item simple text='Actions'>
          <Dropdown.Menu>
            <Dropdown.Item>Add book</Dropdown.Item>
            <Dropdown.Item>Add Review</Dropdown.Item>
            <Dropdown.Divider />
            <Dropdown.Header>Settings</Dropdown.Header>
            <Dropdown.Item>
              <i className='dropdown icon' />
              <span className='text'>Profile</span>
              <Dropdown.Menu>
                <Dropdown.Item>Manage</Dropdown.Item>
                <Dropdown.Item>Delete</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown.Item>
            <Dropdown.Item>Log Out</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
        <Mysearchbar/>
      </Container>
    </Menu>
  </div>
)

export default FixedMenuLayout