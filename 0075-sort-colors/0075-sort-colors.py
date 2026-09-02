class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i=0
        k=0
        j=len(nums)-1
        while k<=j:
            if nums[k]==0:
              nums[i], nums[k]= nums[k],nums[i]
              k+=1
              i+=1
            elif nums[k]==1:
              k+=1
            elif nums[k]==2:
              nums[k], nums[j] = nums[j], nums[k] 
              j-=1
           
                