class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_count = float(inf)
        # if k==len(blocks):
        #     return blocks.count('W')
        # for i in range(len(blocks)-k+1):
        #     count_b = 0
        #     for j in range(k):
        #         if blocks[j+i]=='B':
        #             count_b +=1
        #             if count_b == k:
        #                 return 0
        #     min_count = min(min_count, k - count_b)
        
        # return min_count
        l= 0
        r = k-1
        while r<len(blocks):
            count_w = 0
            for i in range(k):
                if blocks[l+i]=='W':
                    count_w +=1
            l+=1
            r+=1
            min_count = min(count_w,min_count)
        return min_count

