import React from 'react';
import {getBoard} from '../reducers';
import {connect} from 'react-redux';

function App() {
  return <div>Hello world!</div>;
}

function mapStateToProps(state) {
  return {
    board: getBoard(state)
  };
}

export default connect(mapStateToProps)(App);
