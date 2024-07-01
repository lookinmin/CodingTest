from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words = defaultdict(int)
        for w in s:
            words[w] += 1
        
        for w in t:
            if not words[w] or words[w] == 0:
                return False
            else:
                words[w] -= 1

        if sum(list(words.values())) == 0:
            return True
        else:
            return False