class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i=0
        while i*i <=c:
            a= c-i*i
            b=math.sqrt(a)
            if b==int(b):
                return True
            else:
                i+=1
        return False
        
            