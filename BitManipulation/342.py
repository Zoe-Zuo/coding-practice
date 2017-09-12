class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        while n and n%4==0:
            n/=4
        if n==1:
            return True
        else:
            return False