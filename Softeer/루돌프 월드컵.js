var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim();
let teams = input.split(' ').map(Number);
// 이기면 3, 비기면 1, 지면 0
// 총 경기 수 =  1-2.1-3.1-4.2-3.2-4.3-4. : 6번
// 상위 2등 안에 들어야 함

const Prob = (f1, f2) => {
  const win = (4 * f1) / (5 * f1 + 5 * f2);
  const lose = (4 * f2) / (5 * f1 + 5 * f2);
  const draw = (f1 + f2) / (5 * f1 + 5 * f2);
  return { win, lose, draw };
};

const dfs = (game, points, prob) => {
  // 현재 진행한 게임 수, 각 루돌프의 점수, 1번이 1or2등 할 확률
  if (game === 6) {
    const rank = points
      .map((p, i) => ({ score: p, idx: i }))
      .sort((a, b) => b.score - a.score || a.idx - b.idx);
    if (rank[0].idx === 0 || rank[1].idx === 0) {
      // 1이 1등 or 2등
      res += prob;
    }
    return;
  }
  const matches = [
    [0, 1],
    [0, 2],
    [0, 3],
    [1, 2],
    [1, 3],
    [2, 3],
  ];

  const [i, j] = matches[game];
  const { win, lose, draw } = Prob(teams[i], teams[j]);

  // i 승
  points[i] += 3;
  dfs(game + 1, points, prob * win);
  points[i] -= 3;

  // j 승
  points[j] += 3;
  dfs(game + 1, points, prob * lose);
  points[j] -= 3;

  // 비김
  points[i] += 1;
  points[j] += 1;
  dfs(game + 1, points, prob * draw);
  points[i] -= 1;
  points[j] -= 1;
};

var res = 0;
dfs(0, [0, 0, 0, 0], 1);

console.log((res * 100).toFixed(3));
