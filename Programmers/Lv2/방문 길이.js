function solution(dirs) {
  var answer = 0;
  var route = new Set();

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, 1, -1];
  // UDRL

  var x = 0;
  var y = 0;

  for (let d of dirs) {
    let k = -1;
    if (d === 'U') {
      k = 0;
    } else if (d === 'D') {
      k = 1;
    } else if (d === 'R') {
      k = 2;
    } else {
      k = 3;
    }

    let nx = x + dx[k];
    let ny = y + dy[k];

    if (-5 <= nx && nx <= 5 && -5 <= ny && ny <= 5) {
      // 좌표 쌍을 문자열로 저장 (양방향)
      let from = `${x},${y}`;
      let to = `${nx},${ny}`;

      // 경로가 새로운 경로일 때만 저장 (양방향으로 처리)
      let path1 = `${from}->${to}`;
      let path2 = `${to}->${from}`;

      if (!route.has(path1) && !route.has(path2)) {
        route.add(path1);
        route.add(path2);
        answer++; // 새로운 경로일 때만 카운트
      }

      // 위치 업데이트
      x = nx;
      y = ny;
    }
  }
  return answer;
}
