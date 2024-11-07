class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        k = len(arr)
        tmp = []
        for num in arr:
            if num == 0:
                tmp.append(0)
                tmp.append(0)
            else:
                tmp.append(num)
        tmp = tmp[:k]
        arr[:] = tmp