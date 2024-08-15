/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  if (prices.length === 1) {
    return 0;
  }
  const k = prices.length;

  let hold = new Array(k).fill(0);
  // i 번째 날 주식을 가지고 있는 상태에서의 이익
  let sell = new Array(k).fill(0);
  // i 번째 날 주식을 판 상태에서의 이익
  let rest = new Array(k).fill(0);
  // i 번째 날 쉼

  hold[0] = -prices[0]; // 첫 주식 샀다 가정

  for (let i = 1; i < k; i++) {
    hold[i] = Math.max(hold[i - 1], rest[i - 1] - prices[i]);
    // 이전 날에 주식을 갖고있었거나, 쉬고 있던 상태에서 새롭게 주식 구매
    sell[i] = hold[i - 1] + prices[i];
    // 이전날의 값과 오늘 값의 차익 = 매매
    rest[i] = Math.max(rest[i - 1], sell[i - 1]);
  }
  return Math.max(sell[k - 1], rest[k - 1]);
};
