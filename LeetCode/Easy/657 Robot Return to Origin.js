/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function (moves) {
  var now = [0, 0];
  moves = moves.split('');

  for (let move of moves) {
    if (move === 'U') {
      now[0]++;
    } else if (move === 'D') {
      now[0]--;
    } else if (move === 'R') {
      now[1]++;
    } else {
      now[1]--;
    }
  }
  if (now[0] === 0 && now[1] === 0) {
    return true;
  } else {
    return false;
  }
};
