from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []

        starts = sorted((interval[0], idx) for idx, interval in enumerate(intervals))
        
        for interval in intervals:
            end = interval[1]

            idx = bisect_left(starts, (end, ))
            if idx < len(starts):
                res.append(starts[idx][1])
            else:
                res.append(-1)
        
        return res