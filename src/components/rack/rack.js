import React from 'react';
import Cell, {newCell} from '../cell';
import './rack.css';

export function Rack({id, letters, points}) {
  return (
    <div className="rack">
      <div className="player">{'Player ' + id}</div>
      <div className="score">{'Score: ' + points}</div>
      {(letters.length > 0 ? 
        letters.map((l,index) => <Cell row='0' col={index} cell={newCell(l)}/>) : 
        null)}
      {[...Array(7-letters.length).keys()].map((col) => <Cell row='0' col={col+letters.length} cell={newCell()}/>)}
    </div>
  )
}

