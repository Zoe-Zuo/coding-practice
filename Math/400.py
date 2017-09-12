class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        size=1
        while True:
            start=10**(size-1)
            zone=9*10**(size-1)*size
            if n>zone:
                n=n-zone
                size=size+1
                continue
            if n<=zone:
                a=n+size-1
                num=start+a/size-1
                s=str(num)
                d=a%size
                return int(s[d])