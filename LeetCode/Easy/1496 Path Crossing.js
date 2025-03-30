/**
 * @param {string} path
 * @return {boolean}
 */
var isPathCrossing = function (path) {
  let origin = [0, 0];
  let route = new Set(['0,0']);

  for (let i = 0; i < path.length; i++) {
    if (path[i] === 'N') {
      origin[0] -= 1;
    } else if (path[i] === 'S') {
      origin[0] += 1;
    } else if (path[i] === 'E') {
      origin[1] += 1;
    } else {
      origin[1] -= 1;
    }

    const currentPoint = `${origin[0]},${origin[1]}`;
    if (route.has(currentPoint)) {
      return true;
    }
    route.add(currentPoint);
  }
  return false;
};
