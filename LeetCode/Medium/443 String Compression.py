class Solution:
    def compress(self, chars: List[str]) -> int:
        # using two pointer
        r_idx = 0
        w_idx = 0

        n = len(chars)

        while r_idx < n:
            cur = chars[r_idx]
            group_st_idx = r_idx # 현재 연속되는 문자열의 시작 위치

            while r_idx < n and chars[r_idx] == cur:
                r_idx += 1
            
            cnt = r_idx - group_st_idx
            chars[w_idx] = cur
            w_idx += 1
            if cnt > 1:
                for digit in str(cnt):  # 12일 경우, [1, 2]로 입력
                    chars[w_idx] = digit
                    w_idx += 1
        
        return w_idx