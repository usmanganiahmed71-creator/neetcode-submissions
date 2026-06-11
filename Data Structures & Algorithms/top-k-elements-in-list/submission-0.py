from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        return (sorted(counts.keys(),reverse=True,key=lambda x:counts[x])[0:k])