import {combineReducers} from 'redux';
import {createSelector} from 'reselect';
import board, {selectors as boardSelectors} from './board';
import tiles, {selectors as tilesSelectors} from './tiles';
import players, {selectors as playerSelectors} from './players';
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
export const getBoard = state => boardSelectors.getBoard(state.board);
export const getPlayers = state => playerSelectors.getPlayers(state.players);
export const getPlayerId = (state, player) => playerSelectors.getPlayerId(state.players, player);
export const getLetters = (state, player) => playerSelectors.getLetters(state.players, player);
export const getPoints = (state, player) => playerSelectors.getPoints(state.players, player);
export const getSelected = (state, player) => playerSelectors.getSelected(state.players, player);
export const getTiles = (state, count) => tilesSelectors.getTiles(state.tiles, count);
export const getValue = (state, letter) => tilesSelectors.getValue(state.tiles, letter);
