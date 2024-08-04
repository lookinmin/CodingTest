/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function (num1, num2) {
  return (BigInt(num1) + BigInt(num2)).toString();
};

//----------------------------- Without BigInt-------------------------------

/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function (num1, num2) {
  let i = num1.length - 1;
  let j = num2.length - 1;
  let sum = [];
  let carry = 0;

  while (i >= 0 || j >= 0 || carry) {
    let n1 = num1[i] || 0;
    let n2 = num2[j] || 0;

    let cur = parseInt(n1) + parseInt(n2) + carry;
    let remain = cur % 10;

    sum.push(remain);
    carry = cur >= 10 ? 1 : 0;
    j--;
    i--;
  }

  return sum.reverse().join('');
};
