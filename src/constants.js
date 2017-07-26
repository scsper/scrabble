export const ActionTypes = {
  INITIAL_STATE: 'INITIAL_STATE',
  TILE_SELECTED: 'TILE_SELECTED'
};

export const Multipliers = {
  EMPTY: 0,
  DOUBLE_LETTER: 2,
  DOUBLE_WORD: 3,
  TRIPLE_LETTER: 4,
  TRIPLE_WORD: 5
};

export const CellStates = {
  EMPTY: 'EMPTY',
  PENDING: 'PENDING',
  FULL: 'FULL'
};

export const BoardConfigurations = {
  SCRABBLE: [
    [5, 0, 0, 2, 0, 0, 0, 5, 0, 0, 0, 2, 0, 0, 5],
    [0, 3, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 3, 0, 0, 0, 2, 0, 2, 0, 0, 0, 3, 0, 0],
    [2, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 2],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0],
    [0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0],
    [5, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 5],
    [0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0],
    [0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    [2, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 2, 0, 2, 0, 0, 0, 3, 0, 0],
    [0, 3, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 3, 0],
    [5, 0, 0, 2, 0, 0, 0, 5, 0, 0, 0, 2, 0, 0, 5]
  ]
};

export const TileConfigurations = {
  SCRABBLE: [
    {letter: 'a', count: 9, value: 1},
    {letter: 'b', count: 2, value: 3},
    {letter: 'c', count: 2, value: 3},
    {letter: 'd', count: 4, value: 2},
    {letter: 'e', count: 12, value: 1},
    {letter: 'f', count: 2, value: 4},
    {letter: 'g', count: 3, value: 2},
    {letter: 'h', count: 2, value: 4},
    {letter: 'i', count: 9, value: 1},
    {letter: 'j', count: 1, value: 8},
    {letter: 'k', count: 1, value: 5},
    {letter: 'l', count: 4, value: 1},
    {letter: 'm', count: 2, value: 3},
    {letter: 'n', count: 6, value: 1},
    {letter: 'o', count: 8, value: 1},
    {letter: 'p', count: 2, value: 3},
    {letter: 'q', count: 1, value: 10},
    {letter: 'r', count: 6, value: 1},
    {letter: 's', count: 4, value: 1},
    {letter: 't', count: 6, value: 1},
    {letter: 'u', count: 4, value: 1},
    {letter: 'v', count: 2, value: 4},
    {letter: 'w', count: 2, value: 4},
    {letter: 'x', count: 1, value: 8},
    {letter: 'y', count: 2, value: 4},
    {letter: 'z', count: 1, value: 10},
    {letter: 'blank', count: 2, value: 0}
  ]
};
