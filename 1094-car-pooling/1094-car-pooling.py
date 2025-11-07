class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = [] #[(location,+-passengers)]
        for trip in trips:
            events.append([trip[1],trip[0]])     #board
            events.append([trip[2],-trip[0]])    #drop
        events.sort()

        ppl = 0
        for event in events:
            ppl += event[1]
            if ppl>capacity:
                return False
        return True
