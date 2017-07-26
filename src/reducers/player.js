import {ActionTypes} from '../constants';
const {INITIAL_STATE, TILE_SELECTED} = ActionTypes;

export default function player(state = {}, action) {
  if (action.turn !== state.id && action.type !== INITIAL_STATE) {
    return state;
  }

  switch (action.type) {
    case TILE_SELECTED:
      if (state.selected == '') {
        return Object.assign({}, state, {
          selected: action.tileId
        });
      } else {
        var newletter, oldletter, newletters;
        newletter = state.letters[parseInt(action.tileId.substring(2, 3))];
        oldletter = state.letters[parseInt(state.selected.substring(2, 3))];
        newletters = state.letters.slice();
        newletters[parseInt(state.selected.substring(2, 3))] = newletter;
        newletters[parseInt(action.tileId.substring(2, 3))] = oldletter;
        return Object.assign({}, state, {
          letters: newletters,
          selected: ''
        });
      }
    case INITIAL_STATE:
      return {
        id: action.id,
        letters: ['a', 'b', 'c'],
        points: 0,
        selected: ''
      };
    default:
      return state;
  }
}

export const selectors = {
  getId: state => state.id,
  getLetters: state => state.letters,
  getPoints: state => state.points,
  getSelected: state => state.selected
};
