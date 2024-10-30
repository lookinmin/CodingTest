// 오목, S2
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = parseInt(input[0]);

const board = Array.from(Array(20), () => Array(20).fill(0));

// 돌을 놓을 좌표를 배열로 저장
const stones = input.slice(1).map((line) => line.split(' ').map(Number));

// 방향 설정 (대각선 왼쪽 위, 위쪽, 대각선 오른쪽 위, 오른쪽)
const directions = [
  [-1, -1],
  [-1, 0],
  [-1, 1],
  [0, 1],
];

// 범위 체크 함수
const isValid = (x, y) => x >= 0 && x < 20 && y >= 0 && y < 20;

// BFS를 통해 돌의 연속 개수를 확인하는 함수
const bfs = (startX, startY, direction, color) => {
  const queue = [[startX, startY]];
  let count = 1;
  const visited = Array.from(Array(20), () => Array(20).fill(false));
  visited[startX][startY] = true;

  // 두 방향으로 탐색 (주어진 방향과 반대 방향)
  const moves = [direction, [-direction[0], -direction[1]]];
  for (const [dx, dy] of moves) {
    let x = startX + dx;
    let y = startY + dy;

    // 현재 방향으로 연속된 돌을 셈
    while (isValid(x, y) && board[x][y] === color && !visited[x][y]) {
      visited[x][y] = true;
      count++;
      x += dx;
      y += dy;
    }
  }

  return count;
};

// 매 턴마다 돌을 놓고, 오목이 완성되었는지 확인
for (let i = 0; i < n; i++) {
  const [x, y] = stones[i];
  const color = i % 2 === 0 ? 1 : 2; // 홀수번째는 흑돌(1), 짝수번째는 백돌(2)
  board[x][y] = color;

  // 4가지 방향으로 BFS 탐색
  for (const direction of directions) {
    if (bfs(x, y, direction, color) === 5) {
      console.log(i + 1); // 오목이 성립된 수 출력
      process.exit(0); // 프로그램 종료
    }
  }
}

// 오목이 완성되지 않은 경우
console.log(-1);
