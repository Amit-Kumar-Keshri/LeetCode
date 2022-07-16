class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        end = intervals[0]
        ans = 0
        for i in range(1, len(intervals)):
            if end[1] > intervals[i][0]:
                ans += 1
                end[1] = min(intervals[i][1], end[1])
            else:
                end = intervals[i]
        return ans
        