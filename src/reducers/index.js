import {combineReducers} from 'redux';
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

export const getBoard = (state) => boardSelectors.getBoard(state.board);
