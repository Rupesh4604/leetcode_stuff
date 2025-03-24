class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:        
        meetings.sort()

        merged = [meetings[0]]
        for start, end in meetings[1:]:
            last_end = merged[-1][1]
            if start <= last_end:  # Overlapping meetings
                merged[-1][1] = max(last_end, end)  # Merge intervals
            else:
                merged.append([start, end])  # No overlap, add new interval
        
        diff = 0
        diff += merged[0][0] - 1  # Free days before first meeting
        for i in range(len(merged) - 1):
            diff += (merged[i+1][0] - merged[i][1] - 1)
        diff += (days - merged[-1][1])
        return diff