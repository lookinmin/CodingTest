class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        cnt = 10

        if n > 1:
            unique_digits = 9       # 첫번째 자리수는 1~9까지
            can_use = 9             # 두번째 자리수는 첫번째 제외한 0~9 중 9개

            for i in range(2, n + 1):
                unique_digits *= can_use
                cnt += unique_digits
                can_use -= 1        # 세번째 자리수는 8개...
        
        return cnt