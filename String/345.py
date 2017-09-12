class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = list('aeiouAEIOU')
        l, r = 0, len(s)-1
        res=list(s)
        while r>l:
            if res[l] not in vowels:
                l+=1
            if res[r] not in vowels:
                r-=1
            if res[l] in vowels and res[r] in vowels:
                res[l], res[r]=res[r], res[l]
                l+=1
                r-=1
        return ''.join(res)