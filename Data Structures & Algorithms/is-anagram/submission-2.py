from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=Counter(s)
        for a in t:
            if a not in count:
                return False
            else:
                count[a]-=1
                if count[a]==0:
                    count.pop(a)
        return count==dict(())