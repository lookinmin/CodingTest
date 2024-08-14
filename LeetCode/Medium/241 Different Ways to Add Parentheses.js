/**
 * @param {string} expression
 * @return {number[]}
 */
var diffWaysToCompute = function (expression) {
  if (!isNaN(expression)) {
    return [parseInt(expression)];
  }

  let res = [];

  for (let i = 0; i < expression.length; i++) {
    let w = expression[i];
    if (w === '+' || w === '-' || w === '*') {
      let left = diffWaysToCompute(expression.slice(0, i));
      let right = diffWaysToCompute(expression.slice(i + 1));

      for (let l of left) {
        for (let r of right) {
          if (w === '+') {
            res.push(l + r);
          } else if (w === '-') {
            res.push(l - r);
          } else if (w === '*') {
            res.push(l * r);
          }
        }
      }
    }
  }

  return res;
};
