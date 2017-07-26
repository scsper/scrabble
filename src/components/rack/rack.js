import React from 'react';
import Tile from '../tile';
import './rack.css';

export function Rack({id, letters, points}) {
  return (
    <div className="rack">
      <div className="player">
        {'Player ' + id}
      </div>
      <div className="score">
        {'Score: ' + points}
      </div>
      <div className="tiles">
        {letters.map(l => <Tile letter={l} />)}
      </div>
    </div>
  );
}
