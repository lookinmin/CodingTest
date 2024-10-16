function solution(storey) {
  var answer = 0;

  let carry = 0; // 다음 자릿수 올림 값

  while (storey > 0) {
    let digit = storey % 10;
    storey = Math.floor(storey / 10);

    digit += carry;

    if (digit < 5) {
      answer += digit;
      carry = 0;
    } else if (digit > 5) {
      answer += 10 - digit;
      carry = 1;
    } else {
      if (storey % 10 >= 5) {
        answer += 10 - digit;
        carry = 1;
      } else {
        answer += digit;
        carry = 0;
      }
    }
  }

  if (carry > 0) {
    answer += carry;
  }

  return answer;
}
