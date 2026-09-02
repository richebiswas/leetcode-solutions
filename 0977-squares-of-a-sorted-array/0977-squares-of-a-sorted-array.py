class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        i = 0
        j = len(nums) - 1
        k = len(nums) - 1

        ans = [0] * len(nums)

        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                ans[k] = nums[j] ** 2
                j -= 1
                k -= 1
            else:
                ans[k] = nums[i] ** 2
                i += 1
                k -= 1

        return ans