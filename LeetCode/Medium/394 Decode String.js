/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
  var stack = [];
  let tmp = '';
  let num = 0;

  for (let char of s) {
    if (!isNaN(char)) {
      num = num * 10 + parseInt(char);
    } else if (char === '[') {
      stack.push(tmp);
      stack.push(num);
      num = 0;
      tmp = '';
    } else if (char === ']') {
      const value = stack.pop(); // 숫자
      const word = stack.pop();
      tmp = word + tmp.repeat(value);
    } else {
      tmp += char;
    }
  }

  return tmp;
};
