/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function (s, t) {
  var stackS = [];
  var stackT = [];

  for (let w of s) {
    if (w === '#') {
      stackS.pop();
    } else {
      stackS.push(w);
    }
  }

  for (let w of t) {
    if (w === '#') {
      stackT.pop();
    } else {
      stackT.push(w);
    }
  }

  var cvtS = stackS.join();
  var cvtT = stackT.join();

  return cvtS === cvtT;
};
