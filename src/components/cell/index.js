import React from 'react';
import classnames from 'classnames';
import './cell.css';
import {Multipliers, CellStates} from '../../constants';

export default function Cell({cell, row, col}) {
  const classNames = classnames({
    cell: true,
    'double-word': cell.multiplier === Multipliers.DOUBLE_WORD,
    'double-letter': cell.multiplier === Multipliers.DOUBLE_LETTER,
    'triple-word': cell.multiplier === Multipliers.TRIPLE_WORD,
    'triple-letter': cell.multiplier === Multipliers.TRIPLE_LETTER
  });

  return (
    <div className={classNames} id={`${row}_${col}`}>
      {cell.letter !== '' ? cell.letter : ''}
    </div>
  );
}

export function newCell(letter = '') {
  return {
    status: letter === '' ? CellStates.EMPTY : CellStates.FULL,
    multiplier: 0,
    letter: letter
  };
}
