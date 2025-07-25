class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = sorted(nums1)
        self.n = len(nums1)
        self.nums2 = nums2
        self.freq = Counter(nums2)
        self.maxi = max(self.freq.keys())

    def add(self, index: int, val: int) -> None:
        x = self.nums2[index]
        self.freq[x]-=1
        self.nums2[index]+=val
        self.freq[x+val]+=1
        if x+val>self.maxi:
            self.maxi = x + val

    def count(self, tot: int) -> int:
        ans = 0
        i0 = bisect.bisect_left(self.nums1, tot-self.maxi)
        for i in range(i0, self.n):
            y=self.nums1[i]
            if y>=tot: break
            ans+=self.freq[tot-y]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)