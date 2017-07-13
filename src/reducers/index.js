import {combineReducers} from 'redux';
import board from './board';
import tiles from './tiles';

export default combineReducers({
  board,
  tiles
});
