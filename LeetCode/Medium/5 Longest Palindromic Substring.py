class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        max_len = 1
        tmp = s[0]
        k = len(s)
        dp = [[0]* k for _ in range(k)]

        for i in range(k):
            dp[i][i] = 1
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        tmp = s[j : i + 1]
        return tmp     