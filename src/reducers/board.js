import {ActionTypes, BoardConfigurations} from '../constants';
import {initializeBoard} from './helpers/board';

const {INITIAL_STATE} = ActionTypes;

function board(state = [], action) {
  switch (action.type) {
    case INITIAL_STATE:
      return initializeBoard(BoardConfigurations.SCRABBLE);
    default:
      return state;
  }
}

export default board;
