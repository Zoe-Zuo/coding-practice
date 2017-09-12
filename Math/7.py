class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        if x<10:
            return x*sign
        j=0
        while x/10!=0:
            i=x%10
            x/=10
            j=(i+j)*10
            if x/10==0:
                break
        if j+x<2**31-1:
            return sign*(j+x)
        else:
            return 0
                