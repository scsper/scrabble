import React from 'react';
import {getValue} from '../../reducers';
import {connect} from 'react-redux';
import './tile.css';

function Tile({letter, value}) {
  return (
    <div className="tile">
      <div className="value">
        {value}
      </div>
      <div className="letter">
        {letter}
      </div>
    </div>
  );
}

function mapStateToProps(state, l) {
  console.log(l);
  return {
    letter: l.letter,
    value: getValue(state, l.letter)
  };
}

export default connect(mapStateToProps)(Tile)
