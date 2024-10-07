function solution(scoville, K) {
  var cnt = 0;
  scoville.sort((a, b) => a - b);

  const newScoville = [];

  let idx = 0;
  let newIdx = 0;

  const findMin = () => {
    // 두 배열 중 작은 값 찾기
    const a = scoville[idx];
    const b = newScoville[newIdx];

    if (a === undefined) return newScoville[newIdx++];
    if (b === undefined) return scoville[idx++];

    return a < b ? scoville[idx++] : newScoville[newIdx++];
  };

  while (scoville.length - idx + newScoville.length - newIdx > 0) {
    const min1 = findMin();
    if (min1 >= K) return cnt;
    // 가장 작은 값이 K 이상

    const min2 = findMin();
    if (min2 === undefined) return -1;

    const mix = min1 + min2 * 2;
    newScoville.push(mix);
    cnt++;
  }
}
