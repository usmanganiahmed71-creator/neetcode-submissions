class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        post=[1]*len(nums)
        num=1
        for n in range(len(nums)):
            pre[n]=num
            num=nums[n]*num
        num=1
        for n in range(len(nums)-1,-1,-1):
            post[n]=num
            num=nums[n]*num
        ans=[post[m]*pre[m] for m in range(len(nums))]
        return ans