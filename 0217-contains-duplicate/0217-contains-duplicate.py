class Solution(object):
    def containsDuplicate(self, nums):
        dit = set()
        for i in nums:
            if i in dit:
                return True
            else:    
             dit.add(i)
            
        return False 
