class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return False
        prime={}
        i=1
        while i*i<=num:
            if num%i!=0:
                i+=1
            if num%i==0:
                if i not in prime:
                    prime[i]=1
                if num/i not in prime:
                    prime[num/i]=1
                i+=1
        return sum(prime)==2*num
                