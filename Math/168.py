class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=[]
        while n!=0:
            a=(n-1)%26
            temp=chr(a+ord('A'))
            res.append(temp)
            n=(n-1)//26
        res.reverse()
        return ''.join(res)