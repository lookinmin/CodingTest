/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  var stack = [];
  for (let token of tokens) {
    if (token === '+') {
      let num1 = stack.pop();
      let num2 = stack.pop();
      let num = num1 + num2;
      stack.push(num);
    } else if (token === '-') {
      let num1 = stack.pop();
      let num2 = stack.pop();
      let num = num2 - num1;
      stack.push(num);
    } else if (token === '*') {
      let num1 = stack.pop();
      let num2 = stack.pop();
      let num = num1 * num2;
      stack.push(num);
    } else if (token === '/') {
      let num1 = stack.pop();
      let num2 = stack.pop();
      let num = Math.trunc(num2 / num1);
      stack.push(num);
    } else {
      stack.push(parseInt(token));
    }
  }
  return stack[0];
};
