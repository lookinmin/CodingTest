from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        isIn = set()

        for w in s:
            counter[w] -= 1

            if w in isIn:
                continue
            
            while stack and stack[-1] > w and counter[stack[-1]] > 0:
                # 뒤에 현재 stack[-1]의 문자가 남아있음
                # 현재 w가 stack[-1]보다 사전순으로 앞임
                isIn.remove(stack.pop())
            
            stack.append(w)
            isIn.add(w)

        return ''.join(stack)


