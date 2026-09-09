class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1000
        total=0
        while i<=n:
           total+=n-i+1
           i*=1000
        return total    