from collections import deque
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        q = deque(name)
        tq = deque(typed)

        prev = None
        
        while tq:
            if not q:
                if tq[0] == prev:
                    tq.popleft()
                else:
                    return False

            elif q[0] == tq[0]:
                prev = q.popleft()
                tq.popleft()
            
            elif tq[0] == prev:
                tq.popleft()
            else:
                return False
        return not q