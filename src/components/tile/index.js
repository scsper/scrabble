import React from 'react';
import {connect} from 'react-redux';
import {getTiles} from '../../reducers';
import './tile.css';

function Tile({letter}) {
  return (
    <div className="tile">
      {letter}
    </div>
  );
}

function mapStateToProps(state) {
  return {
    tile: getTiles(state, 1)
  };
}

export default connect(mapStateToProps)(Tile);
