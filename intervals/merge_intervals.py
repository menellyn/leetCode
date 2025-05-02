class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                ans.append([start, end])
                start = interval[0]
                end = interval[1]

        ans.append([start, end])

        return ans