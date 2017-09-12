class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return None
        res=0
        for i in range(0,len(s)):
            temp=(ord(s[i])-64)*26**(len(s)-1-i)
            res+=temp
        return res