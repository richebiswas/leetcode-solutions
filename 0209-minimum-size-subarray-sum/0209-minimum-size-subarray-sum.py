class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=0
        result=float('inf')
        sum=0
        while high<len(nums):
            sum+=nums[high]
            while sum>=target:
                result=min(result,high-low+1)
                sum-=nums[low]
                low+=1
            high+=1
        if result==float('inf'):
            return 0
        return result        