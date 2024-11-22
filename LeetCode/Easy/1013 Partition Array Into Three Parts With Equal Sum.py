class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False
        
        target = total // 3
        part = 0

        cnt = 0

        for num in arr:
            part += num
            if part == target:
                cnt += 1
                part = 0
        
        return cnt >= 3