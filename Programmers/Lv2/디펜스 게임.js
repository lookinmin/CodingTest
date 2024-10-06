function solution(n, k, enemy) {
  let [left, right] = [0, enemy.length];

  let mid = Math.floor((left + right) / 2);

  while (left <= right) {
    const curSlice = enemy.slice(0, mid).sort((a, b) => b - a);
    // 이번 탐색에서 사용될 범위 내림차순 정렬
    let noDie = k;

    const curEnemy = curSlice.reduce((acc, cur) => {
      if (noDie > 0) {
        noDie--;
        return acc;
      }
      return acc + cur;
    }, 0);
    // 무적권을 갯수만큼 소진하고 남은 병사 수 합산

    if (n - curEnemy >= 0 && noDie >= 0) {
      // n이 현재 탐색 범위의 병사 수 보다 많고, 무적권을 전부 소진하지 않음 => 더 많은 라운드 진행 가능
      left = mid + 1;
    } else {
      // 현재 탐색 범위 [0 ~ mid] 까지의 round 진행 불가, mid를 줄여야 함
      right = mid - 1;
    }
    mid = Math.floor((left + right) / 2);
  }
  return left - 1;
}
