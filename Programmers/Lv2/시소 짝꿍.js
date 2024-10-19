function solution(weights) {
  var answer = 0;
  var n = weights.length;
  // 2, 3, 4
  var dic = new Map();

  for (let weight of weights) {
    dic.set(weight, (dic.get(weight) || 0) + 1);
  }
  for (let [key, value] of dic) {
    if (value > 1) {
      answer += Math.floor((value * (value - 1)) / 2);
    }
    if (dic.has(key * 2)) {
      answer += value * dic.get(key * 2);
    }
    if ((key * 3) % 2 === 0 && dic.has((key * 3) / 2)) {
      answer += value * dic.get(Math.floor((key * 3) / 2));
    }
    if ((key * 4) % 3 === 0 && dic.has((key * 4) / 3)) {
      answer += value * dic.get(Math.floor((key * 4) / 3));
    }
  }
  return answer;
}
