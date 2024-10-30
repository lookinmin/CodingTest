function solution(arr) {
  var answer = [0, 0];
  let n = arr.length;

  const check = (x, y, n) => {
    const start = arr[x][y];
    for (let i = x; i < x + n; i++) {
      for (let j = y; j < y + n; j++) {
        if (arr[i][j] !== start) {
          return -1;
        }
      }
    }
    return start;
  };

  const divideAndCount = (x, y, n) => {
    if (n === 1) {
      // 기저 조건: 최소 영역에 도달한 경우 처리
      answer[arr[x][y]]++;
      return;
    }

    const tmp = check(x, y, n);

    if (tmp !== -1) {
      answer[tmp]++;
    } else {
      let half = n / 2;
      divideAndCount(x, y, half);
      divideAndCount(x, y + half, half);
      divideAndCount(x + half, y, half);
      divideAndCount(x + half, y + half, half);
    }
  };

  divideAndCount(0, 0, n);
  return answer;
}
