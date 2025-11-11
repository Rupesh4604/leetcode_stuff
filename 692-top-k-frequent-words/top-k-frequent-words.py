class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        res = sorted(counts,key=lambda x: (-counts[x], x))[:k]
        return res