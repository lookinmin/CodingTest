/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function (word) {
  var isUpper = word.toUpperCase();
  var isLower = word.toLowerCase();
  var isCapital = word[0].toUpperCase() + word.slice(1).toLowerCase();

  if (word === isUpper || word === isLower || word === isCapital) {
    return true;
  } else {
    return false;
  }
};
