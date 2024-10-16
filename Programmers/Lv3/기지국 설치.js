function solution(n, stations, w) {
  var answer = 0;
  let now = 1;

  const coverage = 2 * w + 1;

  for (let station of stations) {
    let start = station - w;
    let end = station + w;

    if (now < start) {
      let gap = start - now;
      answer += Math.ceil(gap / coverage);
    }

    now = end + 1;
  }

  if (now <= n) {
    let gap = n - now + 1;
    answer += Math.ceil(gap / coverage);
  }

  return answer;
}
