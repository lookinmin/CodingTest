class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt = s.count('A')
        if cnt >= 2:
            return False
        for i in range(len(s) - 2):
            if s[i] == 'L':
                tmp = 0
                for j in range(i, i + 3):
                    if s[j] == 'L':
                        tmp+=1
                if tmp >= 3:
                    return False
        
        return True