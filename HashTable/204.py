class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        prime=[True]*n
        prime [0]=prime [1]=False
        for i in xrange(2,n):
            if prime[i] is True:
                for j in xrange(2,(n-1)/i+1):
                    prime[i*j]=False
        return sum (prime)
                    