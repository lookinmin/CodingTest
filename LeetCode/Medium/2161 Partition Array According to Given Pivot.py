class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []

        left = []
        same = []
        right = []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                same.append(num)
            else:
                right.append(num)
        
        res = left + same + right
        return res