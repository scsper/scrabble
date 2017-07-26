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

// results in an api like boardSelectors.getBoard(state.board);
export const selectors = {
  getBoard: state => state
};

// alternate way to write selectors
// results in an api like boardSelectors(state.board).getBoard()
/*
export const selectors = (state = {}) => ({
  getBoard: () => state
});
*/
export default board;
