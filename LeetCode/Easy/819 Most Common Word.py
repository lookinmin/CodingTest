from collections import defaultdict
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[!?\',;.]', ' ', paragraph)
        para = paragraph.lower().split(' ')
        dic = defaultdict(int)

        for s in para:
            if s not in banned and s != '':
                dic[s] += 1
        
        res = sorted(dic.items(), key = lambda x : x[1], reverse = True)
        return res[0][0]