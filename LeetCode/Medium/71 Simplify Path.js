/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function (path) {
  let stack = [];
  let tmp = path.split('/');

  for (let dir of tmp) {
    if (dir === '.' || !dir) {
      continue;
    } else if (dir === '..') {
      if (stack.length > 0) {
        stack.pop();
      }
    } else {
      stack.push(dir);
    }
  }

  let res = '/' + stack.join('/');
  return res;
};
