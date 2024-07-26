from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers) - 1

        while idx1 < idx2:
            tmp = numbers[idx1] + numbers[idx2]
            if tmp == target:
                return [idx1 + 1, idx2 + 1]
            elif tmp < target:
                idx1 += 1
            else:
                idx2 -= 1