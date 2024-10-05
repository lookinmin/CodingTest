function solution(clothes) {
  var cabinet = {};

  clothes.forEach((v) => {
    if (v[1] in cabinet) {
      cabinet[v[1]] += 1;
    } else {
      cabinet[v[1]] = 1;
    }
  });

  var answer = 1;
  for (let tmp of Object.values(cabinet)) {
    answer *= tmp + 1;
  }
  answer -= 1;

  return answer;
}
