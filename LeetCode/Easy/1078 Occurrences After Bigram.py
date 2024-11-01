class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        stack = []
        res = []

        for w in text.split(' '):
            stack.append(w)
            if len(stack) == 3:  # 세 개의 단어가 쌓인 경우
                if stack[0] == first and stack[1] == second:
                    res.append(stack[2])  # 세 번째 단어를 결과에 추가
                stack.pop(0)  # 첫 번째 단어 제거하여 슬라이딩 윈도우 유지

        return res
