/**
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
  var stack = [];
  var currentNumber = 0;
  var operation = '+';

  for (let idx = 0; idx <= s.length; idx++) {
    const char = s[idx];

    if (char >= '0' && char <= '9') {
      currentNumber = currentNumber * 10 + parseInt(char); // 여러 자리 숫자를 처리
    }

    if (((char < '0' || char > '9') && char !== ' ') || idx === s.length) {
      if (operation === '+') {
        stack.push(currentNumber);
      } else if (operation === '-') {
        stack.push(-currentNumber);
      } else if (operation === '*') {
        stack.push(stack.pop() * currentNumber);
      } else if (operation === '/') {
        stack.push(Math.trunc(stack.pop() / currentNumber));
      }
      operation = char; // 현재 연산을 다음 연산으로 업데이트
      currentNumber = 0; // 현재 숫자를 초기화
    }
  }

  return stack.reduce((a, b) => a + b, 0); // 스택의 모든 값을 더해서 결과를 반환
};
