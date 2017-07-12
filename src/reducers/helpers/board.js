import {CellStates} from '../../constants';

export function initializeBoard(configuration) {
  return configuration.map(row =>
    row.map(value => ({
      status: CellStates.EMPTY,
      multiplier: value,
      letter: ''
    }))
  );
}
