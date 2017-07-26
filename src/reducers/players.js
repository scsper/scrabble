import {ActionTypes} from '../constants';
import player, {selectors as playerSelectors} from './player';

const {INITIAL_STATE, TILE_SELECTED} = ActionTypes;

export default function players(state = {}, action) {
  switch (action.type) {
    case TILE_SELECTED:
      action.turn = parseInt(action.player);
      return Object.assign({}, state, {
        1: player(state[1], action),
        2: player(state[2], action)
      });
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
  getPlayerId: (state, id) => playerSelectors.getId(state[id]),
  getLetters: (state, id) => playerSelectors.getLetters(state[id]),
  getPoints: (state, id) => playerSelectors.getPoints(state[id]),
  getSelected: (state, id) => playerSelectors.getSelected(state[id])
};
