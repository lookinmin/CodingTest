/**
 * @param {number} n
 * @return {boolean}
 */
var divisorGame = function (n) {
  var dp = new Array(n + 1).fill(false);

  for (let i = 2; i <= n; i++) {
    for (let j = 1; j < i; j++) {
      if (i % j === 0 && !dp[i - j]) {
        // choosing any x with n % x === 0
        // dp[i-j] <- 현재 플레이어가 j를 선택한 후, 남은 숫자 i-j에서 상대방이 이길 수 있는지에 대한 여부부
        dp[i] = true;
        break;
      }
    }
  }

  return dp[n];
};
