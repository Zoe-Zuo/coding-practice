class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count=0
        while x or y:
            count+=(x&1)^(y&1)
            x>>=1
            y>>=1
        return count