class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w=set()
        le=0
        l=0
        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l+=1
            if s[r] not in w:
                w.add(s[r])
                le=max(le,r-l+1)
        return le