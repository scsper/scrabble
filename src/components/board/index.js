import React from 'react';
import {getBoard} from '../../reducers';
import {connect} from 'react-redux';
import Cell from '../cell';
import './board.css';

function Board({board}) {
  return (
    <div className="board">
      {board.map((row, rowIndex) => row.map((cell, colIndex) => <Cell row={rowIndex} col={colIndex} cell={cell} />))}
    </div>
  );
}

function mapStateToProps(state) {
  return {
    board: getBoard(state)
  };
}

export default connect(mapStateToProps)(Board);
