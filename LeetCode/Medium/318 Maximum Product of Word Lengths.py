class Solution:
    def maxProduct(self, words: List[str]) -> int:
        k = len(words)
        bitmasks = [0] * k
        lengths = [0] * k

        for i in range(k):
            tmp = 0
            for ch in words[i]:
                tmp |= 1 << (ord(ch) - ord('a'))
            bitmasks[i] = tmp
            lengths[i] = len(words[i])
        
        res = 0

        for i in range(k):
            for j in range(i + 1, k):
                if bitmasks[i] & bitmasks[j] == 0:
                    res = max(res, lengths[i] * lengths[j])
        
        return res
