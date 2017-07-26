import React from 'react';
import Cell, {newCell} from '../cell';
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
      {letters.map((l, index) => <Cell row="0" col={index} cell={newCell(l)} />)}
    </div>
  );
}
