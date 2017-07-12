import {ActionTypes, CellStates} from '../../constants';
import reducer from '../board';

const {INITIAL_STATE} = ActionTypes;

describe('src/reducers/board', function() {
  describe(INITIAL_STATE, function() {
    it('initializes a scrabble board', function() {
      const state = reducer({}, {type: INITIAL_STATE});

      state.forEach((row, rowIndex) =>
        row.forEach((cell, colIndex) => {
          expect(cell.status).toBe(CellStates.EMPTY);
          expect(cell.letter).toBe('');

          // we're going to assume that the board is laid out correctly in our configuration.
          expect(cell.multiplier).toBeGreaterThanOrEqual(0);
          expect(cell.multiplier).toBeLessThanOrEqual(5);
        })
      );
    });
  });
});
