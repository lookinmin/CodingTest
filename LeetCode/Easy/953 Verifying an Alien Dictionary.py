from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderTable = dict()

        for i in range(len(order)):
            orderTable[order[i]] = i
        
        for i in range(len(words) - 1):
            now = words[i]
            nxt = words[i + 1]

            for idx in range(min(len(now), len(nxt))):
                if now[idx] != nxt[idx]:
                    if orderTable[now[idx]] < orderTable[nxt[idx]]:
                        break
                    elif orderTable[now[idx]] > orderTable[nxt[idx]]:
                        return False
            else: 
                if len(now) > len(nxt):
                    return False

        return True