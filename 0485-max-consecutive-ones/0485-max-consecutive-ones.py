class Solution(object):
  def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        cnt = 0
        max_cnt = 0

        while i < len(nums):
            if nums[i] == 1:
                cnt += 1

                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0

            i += 1

        return max_cnt