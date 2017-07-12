import {ActionTypes} from '../../constants';
import reducer from '../tiles';

const {INITIAL_STATE} = ActionTypes;

describe('src/reducers/tiles', function() {
  describe(INITIAL_STATE, function() {
    it('initializes the tiles', function() {
      const state = reducer({}, {type: INITIAL_STATE});

      expect(state.bag.length).toBe(100);
      expect(state.values).toEqual({
        a: 1,
        b: 3,
        blank: 0,
        c: 3,
        d: 2,
        e: 1,
        f: 4,
        g: 2,
        h: 4,
        i: 1,
        j: 8,
        k: 5,
        l: 1,
        m: 3,
        n: 1,
        o: 1,
        p: 3,
        q: 10,
        r: 1,
        s: 1,
        t: 1,
        u: 1,
        v: 4,
        w: 4,
        x: 8,
        y: 4,
        z: 10
      });
    });
  });
});
