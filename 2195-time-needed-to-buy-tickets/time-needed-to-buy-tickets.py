class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        t = 0
        while True:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    t += 1
                if i == k and tickets[i] == 0:
                    return t
        # count = 0
        # maxi = tickets[k] 
        # for i in range(k):
        #     if tickets[i]<=maxi:
        #         count +=tickets[i]
        #     else:
        #         count +=maxi
        # for j in range(k,len(tickets)):
        #     if tickets[j]<=maxi:
        #         count +=(tickets[j])
        #     else:
        #         count +=(maxi-1)
        # return count