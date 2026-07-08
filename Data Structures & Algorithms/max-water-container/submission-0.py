class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        maxs=0
        r=len(heights)-1
        while(l<r):
            if maxs<min(heights[l],heights[r])*(r-l):
                maxs=min(heights[l],heights[r])*(r-l)
            if heights[l]>=heights[r]:
                r-=1
            else:
                l+=1
        return maxs