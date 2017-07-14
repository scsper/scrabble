import {combineReducers} from 'redux';
import board, {selectors as boardSelectors} from './board';
import tiles from './tiles';

export default combineReducers({
  board,
  tiles
});

export const getBoard = (state) => boardSelectors.getBoard(state.board);
