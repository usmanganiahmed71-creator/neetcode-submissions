from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        li=[[]for _ in range(len(nums)+1)]
        counts=Counter(nums)
        for c in counts:
            li[counts[c]].append(c)
        ans=[]
        for l in range(len(nums),-1,-1):
            if li[l]!=[]:
                for _ in range(len(li[l])):
                    ans.append(li[l][_])
        return ans[:k]