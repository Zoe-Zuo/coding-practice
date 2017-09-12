class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i,j=1,n
        while i+1<j:
            mid=(i+j)//2
            if (mid*(mid+1))//2<=n:
                i=mid
            else:
                j=mid
        return j if (j*(j+1))//2<=n else i
    
     