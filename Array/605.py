class Solution(object):
    def canPlaceFlowers(self, A, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in xrange(0, len(A)):
            if (A[i]==0 and (i==0 or A[i-1]==0) and (i==len(A)-1 or A[i+1]==0)):
                A[i]=1
                n-=1
        return n<=0