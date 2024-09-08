from collections import deque
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # <- 로 시프트
        s = deque(s)
        goal = deque(goal)
        for i in range(len(s)):
            if s == goal:
                return True
            else:
                val = s.popleft()
                s.append(val)
        
        return False