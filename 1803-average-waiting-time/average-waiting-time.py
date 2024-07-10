class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr = customers[0][0]
        wait = 0
        for i in range(len(customers)):
            start = customers[i][0]
            if start>curr:
                wait+=(customers[i][1])
                curr = start + customers[i][1]
            else:
                wait += (curr - start + customers[i][1])
                curr = curr + customers[i][1]
        return wait/len(customers)
