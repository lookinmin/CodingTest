class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)

        if n != m:
            return False
        
        if s == goal and len(set(s)) < len(s):
            # s에 중복된 문자가 있음
            return True
        
        diff = []

        for i in range(n):
            if s[i] != goal[i]:
                diff.append(i)
        
        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
