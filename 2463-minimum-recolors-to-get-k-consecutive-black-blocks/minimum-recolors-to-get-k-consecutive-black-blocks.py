class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_count = float(inf)
        if k==len(blocks):
            return blocks.count('W')
        for i in range(len(blocks)-k+1):
            count_b = 0
            for j in range(k):
                if blocks[j+i]=='B':
                    count_b +=1
                    if count_b == k:
                        return 0
            min_count = min(min_count, k - count_b)
        
        return min_count

