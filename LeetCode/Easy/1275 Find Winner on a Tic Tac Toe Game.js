/**
 * @param {number[][]} moves
 * @return {string}
 */
var tictactoe = function (moves) {
  var grid = Array.from(Array(3), () => Array(3).fill(0));

  for (let i = 0; i < moves.length; i++) {
    let x = moves[i][0];
    let y = moves[i][1];
    if (i % 2 === 0) {
      grid[x][y] = 1;
    } else {
      grid[x][y] = 2;
    }
  }

  const res = check(grid);
  if (res === 1) {
    return 'A'; // Player A wins
  } else if (res === 2) {
    return 'B'; // Player B wins
  } else if (moves.length === 9) {
    return 'Draw'; // All cells are filled, but no winner
  } else {
    return 'Pending'; // Game not yet finished
  }
};

const check = (grid) => {
  for (let i = 0; i < 3; i++) {
    if (
      grid[i][0] !== 0 &&
      grid[i][0] === grid[i][1] &&
      grid[i][1] === grid[i][2]
    ) {
      return grid[i][0];
    }
    if (
      grid[0][i] !== 0 &&
      grid[0][i] === grid[1][i] &&
      grid[1][i] === grid[2][i]
    ) {
      return grid[0][i];
    }
  }

  if (
    grid[0][0] !== 0 &&
    grid[0][0] === grid[1][1] &&
    grid[1][1] === grid[2][2]
  ) {
    return grid[0][0];
  }
  if (
    grid[0][2] !== 0 &&
    grid[0][2] === grid[1][1] &&
    grid[1][1] === grid[2][0]
  ) {
    return grid[0][2];
  }

  return 0;
};
