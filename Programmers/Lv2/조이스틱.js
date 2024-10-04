function solution(name) {
  const k = name.length;
  // 'A'.charCodeAt() === 65, Z === 90
  var res = 0;
  // 각 알파벳 변경 횟수
  for (let i = 0; i < k; i++) {
    if (name[i] === 'A') {
      continue;
    } else {
      let cnt = Math.min(
        Math.abs(name[i].charCodeAt() - 65),
        Math.abs(90 - name[i].charCodeAt() + 1),
      );
      res += cnt;
    }
  }

  let move = k - 1;
  // 직진만, 후진만 했을 경우의 최소 이동 값

  for (let i = 0; i < k; i++) {
    let nxtIdx = i + 1;
    while (nxtIdx < k && name[nxtIdx] === 'A') {
      nxtIdx++;
      // 'A' 연속 구간 찾기
    }

    // 앞으로 갔다가 뒤로 돌아옴
    move = Math.min(move, i * 2 + k - nxtIdx);
    // i * 2 : 처음부터 i번째까지 왕복 값
    // k - nxtIdx : 마지막 'A'가 아닌 문자까지 이동 값

    // 뒤로 갔다가 다시 앞으로
    move = Math.min(move, (k - nxtIdx) * 2 + i);
  }

  return res + move;
}
