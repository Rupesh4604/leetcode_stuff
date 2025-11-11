class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        # Sort by: frequency ↓ (negative for descending), then lexicographically ↑
        res = sorted(counts,key=lambda x: (-counts[x], x))[:k]
        return res