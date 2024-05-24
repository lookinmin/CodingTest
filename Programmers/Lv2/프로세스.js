function solution(priorities, location) {
  var answer = 0;
  var q = [];

  for (let i = 0; i < priorities.length; i++) {
    q.push([priorities[i], i]);
  }

  while (q.length > 0) {
    var now = q[0];
    var maxval = Math.max(...q.map((e) => e[0]));
    if (now[0] >= maxval && now[1] == location) {
      break;
    } else if (now[0] >= maxval && now[1] != location) {
      answer++;
      q.shift();
    } else {
      var tmp = q.shift();
      q.push(tmp);
    }
  }
  return answer + 1;
}
