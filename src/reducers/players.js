import {ActionTypes} from '../constants';
import player, {selectors as playerSelectors} from './player';

const {INITIAL_STATE} = ActionTypes;

export default function players(state = {}, action) {
  switch (action.type) {
    case INITIAL_STATE:
      return {
        1: player({}, {...action, id: 1}),
        2: player({}, {...action, id: 2})
      };
    default:
      return state;
  }
}

export const selectors = {
  getPlayers: state => state,
  getLetters: (state, id) => playerSelectors.getLetters(state[id])
};
