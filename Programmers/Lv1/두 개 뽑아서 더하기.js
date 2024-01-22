const combinations = (arr, n) => {
  if (n === 1) {
    return arr.map((item) => [item]);
  }
  let result = [];

  arr.forEach((item, idx, origin) => {
    const smallCom = combinations(origin.slice(idx + 1), n - 1);
    smallCom.forEach((smallCom) => {
      result.push([item].concat(smallCom));
    });
  });
  return result;
};

function solution(numbers) {
  var answer = [];
  var tmp = combinations(numbers, 2);

  var res = tmp.map((item) => item[0] + item[1]);
  res.sort((a, b) => a - b);
  var toSet = new Set(res);
  answer = Array.from(toSet);
  return answer;
}
