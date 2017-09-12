class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x<10:
            return True
        x=str(x)
        for i in range(0,len(x)-1):
            if x[i]==x[len(x)-1-i]:
                continue
            else:
                return False
        return True