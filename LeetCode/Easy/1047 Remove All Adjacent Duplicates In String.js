/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function (s) {
  let stack = [];
  for (let w of s) {
    if (stack.length > 0 && stack[stack.length - 1] === w) {
      stack.pop();
    } else {
      stack.push(w);
    }
  }
  return stack.join('');
};
