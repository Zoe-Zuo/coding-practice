class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(s)
        if len(s)==s.count(' '):
            return 0
        stack=[]
        while s[len(s)-1]==' ':
            s=s[0:len(s)-1]
        while s[0]==' ':
            s=s[1:len(s)]
        for i in range(0,len(s)):
            if s[i]!=' ':
                stack.append(s[i])
            else:
                stack=[]
        return len(stack)
            
                
                