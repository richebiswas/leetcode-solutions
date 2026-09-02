class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
           
            k=i+1
            j=len(nums)-1

            while k<j:
                total=nums[i]+nums[j]+nums[k]
                if total==target:
                    return total

                elif abs(total-target)< abs(closest-target):
                   closest=total

                if  total>target:
                    j-=1

                else:
                    k+=1
        return closest                    