function solution(participant, completion) {
  var match = new Map();
  for (p of participant) {
    match.set(p, (match.get(p) || 0) + 1);
  }
  for (c of completion) {
    match.set(c, match.get(c) - 1);
  }
  for (item of match.entries()) {
    if (item[1] === 1) {
      return item[0];
    }
  }
}
