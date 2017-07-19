import {combineReducers} from 'redux';
import {createSelector} from 'reselect';
import board, {selectors as boardSelectors} from './board';
import tiles from './tiles';
import players from './players';
import turn from './turn';

export default combineReducers({
  board,
  tiles,
  players,
  turn
});

// results in an api like selectors(state).getBoard();
// alternate way to write selectors
/*
export const selectors = createSelector(
  state => state,
  state => {
    return {
      getBoard: boardSelectors.getBoard(state.board)
    };
  }
);
*/

// results in an api like getBoard(state);
export const getBoard = (state) => boardSelectors.getBoard(state.board);
