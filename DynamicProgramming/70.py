class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 or n==2:
            return n
        a=1;
        b=2;
        for i in xrange(3,n+1):
            temp = a+b
            a = b
            b = temp
        return b