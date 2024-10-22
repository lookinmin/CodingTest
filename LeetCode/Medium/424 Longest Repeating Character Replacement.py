from collections import defaultdict, Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_cnt = 0
        counter = Counter()
        max_len = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            max_cnt = max(max_cnt, counter[s[right]])

            if(right - left + 1) - max_cnt > k:
                # 현재 문자열 길이에서 가장 많이 등장하는 문자의 빈도 제외
                # 그 길이가 k 초과 -> left 당김
                counter[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len