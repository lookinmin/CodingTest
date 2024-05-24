function solution(s) {
  var answer = true;

  var stack = new Array();

  for (w of s) {
    if (w === "(") {
      stack.push("(");
    } else {
      if (stack.length == 0) {
        return false;
      }
      stack.pop();
    }
  }

  if (stack.length > 0) {
    return false;
  }

  return answer;
}
