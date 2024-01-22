function solution(arr) {
  var answer = [];
  for (num of arr) {
    if (answer.length > 0) {
      let tmp = answer[answer.length - 1];
      if (tmp !== num) {
        answer.push(num);
      }
    } else {
      answer.push(num);
    }
  }
  return answer;
}
