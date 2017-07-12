export function initializeTileValues(configuration) {
  return configuration.reduce((values, config) => {
    values[config.letter] = config.value;

    return values;
  }, {});
}

export function initializeTileBag(configuration) {
  const letters = configuration.reduce((letters, config) => {
    for (let i = 0; i < config.count; i++) {
      letters.push(config.letter);
    }

    return letters;
  }, []);

  return shuffleLetters(letters);
}

function shuffleLetters(letters) {
  const shuffledLetters = [];

  while (letters.length) {
    const index = getRandomInt(letters.length);

    shuffledLetters.push(letters[index]);
    letters.splice(index, 1);
  }

  return shuffledLetters;
}

/**
 * This function is simplified from the example given on MDN:
 * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
 *
 * @param {Number} upperBound The top bound that this function will return, exclusive.
 *   So, if `upperBound` is 20, the maximum value that this function will return is 19.
 * @return {Number} between [0, upperBound].  0 is inclusive, upperBound is exclusive.
 */
function getRandomInt(upperBound) {
  return Math.floor(Math.random() * upperBound);
}
