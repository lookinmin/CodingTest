class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = sum(aliceSizes)
        b = sum(bobSizes)

        diff = (a - b) // 2
        # 교환할 값의 차이

        setA = set(aliceSizes)

        for num in bobSizes:
            tmp = num + diff
            if tmp in setA:
                return [tmp, num]


        