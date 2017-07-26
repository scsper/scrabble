import React from 'react';
import {Rack} from './rack';
import {getPlayers} from '../../reducers';
import {connect} from 'react-redux';
import './racks.css';

function Racks({players}) {
  return (
    <div className="racks">
      {players.map((id) => <Rack id={id.id} letters={id.letters} points={id.points}/>)}
    </div>
  );
}

function mapStateToProps(state) {
  return {
    players: getPlayers(state)
  };
}

export default connect(mapStateToProps)(Racks);
