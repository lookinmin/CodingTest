function solution(money) {
  const n = money.length;

  if (n === 3) return Math.max(...money);
  // 3개면 어차피 하나밖에 못텀

  const robLinear = (start, end) => {
    const dp = new Array(end - start).fill(0);
    dp[0] = money[start];
    dp[1] = Math.max(money[start], money[start + 1]);

    for (let i = 2; i < end - start; i++) {
      dp[i] = Math.max(dp[i - 1], dp[i - 2] + money[start + i]);
    }

    return dp[end - start - 1];
  };

  const withFirst = robLinear(0, n - 1);
  const withoutFirst = robLinear(1, n);

  return Math.max(withFirst, withoutFirst);
}

// LeetCode HouseRobber2와 유사
// dp 배열 선언 과정에서 시작, 끝 인덱스를 지정해서 넘겨줘야함
