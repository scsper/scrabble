import React from 'react';
import {getValue, getSelected} from '../../reducers';
import {connect} from 'react-redux';
import tileActionCreators from '../../action_creators/tile';
import {bindActionCreators} from 'redux';
import './tile.css';

function Tile({id, letter, value, selected, selectTile}) {
  const classes = 'button' + (selected == id ? ' selected' : '');
  return (
    <button className={classes} id={id} onClick={() => selectTile({tileId: id, player: id.substring(0, 1)})}>
      <div className="tile">
        <div className="value">
          {value}
        </div>
        <div className="letter">
          {letter}
        </div>
      </div>
    </button>
  );
}

function mapStateToProps(state, l) {
  console.log(l);
  return {
    letter: l.letter,
    value: getValue(state, l.letter),
    selected: getSelected(state, parseInt(l.id.substring(0, 1)))
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(tileActionCreators, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(Tile);
