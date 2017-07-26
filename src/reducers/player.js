import {ActionTypes} from '../constants';
const {INITIAL_STATE} = ActionTypes;

export default function player(state = {}, action) {
  if (action.turn !== state.id && action.type !== INITIAL_STATE) {
    return state;
  }

  switch (action.type) {
    case INITIAL_STATE:
      return {
        id: action.id,
        letters: ['a','b','c'],
        points: 0
      };
    default:
      return state;
  }
}
