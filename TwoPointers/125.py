class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        alph=[]
        s=s.lower()
        for char in s:
            if char.isalpha() or char.isdigit():
                alph.append(char)
        for i in range(0,len(alph)):
            end=len(alph)-i-1
            if alph[i]!=alph[end]:
                return False
        return True