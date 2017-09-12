class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        max=0x7fffffff
        mask=0xffffffff
        while b!=0:
            a,b=(a^b)&mask, ((a&b)<<1)&mask
        return a if a<=max else ~(a^mask)