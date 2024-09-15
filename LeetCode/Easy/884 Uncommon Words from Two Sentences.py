class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        table = defaultdict(int)
        table2 = defaultdict(int)

        cvt1 = s1.split(' ')
        cvt2 = s2.split(' ')
        
        res = []
        for w in cvt1:
            if w not in cvt2:
                table[w] += 1
            
        for w in cvt2:
            if w not in cvt1:
                table2[w] += 1
        
        for key, value in table.items():
            if value == 1:
                res.append(key)
        for key, value in table2.items():
            if value == 1:
                res.append(key)
        
        return res
        