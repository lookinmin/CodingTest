class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(x, y):
                return all(s[idx] == s[y - idx + x] for idx in range(x, y))
                # x(시작)부터 y(끝)까지 반복하면서 같은지 확인
                # 하나라도 다르면 false 리턴

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return check(left + 1, right) or check(left, right - 1)
            left += 1
            right -= 1
        return True