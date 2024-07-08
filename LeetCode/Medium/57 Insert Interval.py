class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = 0
        
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            # 그냥 push
            res.append(intervals[idx])
            idx += 1
        
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            # 지금 탐색 [a, b], newInterval [n, m] 에서 m >= a 일때
            newInterval = [min(newInterval[0], intervals[idx][0]), max(newInterval[1], intervals[idx][1])]
            idx += 1
        res.append(newInterval)

        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1
        return res