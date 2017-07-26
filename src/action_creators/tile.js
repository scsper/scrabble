import {ActionTypes} from '../constants';

export function selectTile(tileId) {
  return {
    type: ActionTypes.TILE_SELECTED,
    ...tileId
  };
}

export default {selectTile};
