class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        cvt = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        res = []

        def dfs(comb, nxt):
            if not nxt:
                res.append(comb)
                return
            
            for w in cvt[nxt[0]]:
                dfs(comb + w, nxt[1:])
        
        dfs("", digits)
        return res
