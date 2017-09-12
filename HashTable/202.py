class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem=set()
        while n!=1:
            if n in mem:
                return False
            mem.add(n)
            n=sum([int(i)**2 for i in str(n)])
        return True
        