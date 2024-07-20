class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        prev = prices[0]
        for i in range(1, len(prices)):
            now = prices[i]
            if now > prev:
                total += (now - prev)
                prev = now
            else:
                prev = now
                continue
            
        return total
