import React from 'react';
import Tile from '../tile';
import {getValue} from '../../reducers';
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
        {letters.map((l, index) => <Tile key={index} letter={l} />)}
      </div>
    </div>
  );
}
