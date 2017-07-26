import React from 'react';
import classnames from 'classnames';
import './cell.css';
import {Multipliers} from '../../constants';

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
      <div className="letter">
        {cell.letter || ''}
      </div>
    </div>
  );
}
