class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []

        idx = 0
        while idx < len(s):
            pointer = idx
            while pointer < len(s) and s[idx] == s[pointer]:
                pointer += 1
            
            if pointer - idx >= 3:
                res.append([idx, pointer - 1])
            
            idx = pointer
        
        return res