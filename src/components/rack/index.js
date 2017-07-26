import React from 'react';
import {Rack} from './rack';
import {getPlayers} from '../../reducers';
import {connect} from 'react-redux';
import './racks.css';

function Racks({players}) {
  return (
    <div className="racks">
      {players.map(player => <Rack id={player.id} letters={player.letters} points={player.points} />)}
    </div>
  );
}

function mapStateToProps(state) {
  return {
    players: getPlayers(state)
  };
}

export default connect(mapStateToProps)(Racks);
