class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        end = intervals[0]
        ans = 0
        for i in intervals[1:]:
            if end[1] > i[0]:
                ans += 1
                end[1] = min(i[1], end[1])
            else:
                end = i
        return ans
        