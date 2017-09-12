class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(0,len(digits)):
            num=num+digits[i]*10**(len(digits)-1-i)
        res=num+1
        a = []
        s=str(res)
        b = list(s)
        for i in xrange(0, len(b)):
            a.append(int(b[i]))
        return a
            
            
