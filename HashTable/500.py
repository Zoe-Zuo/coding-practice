class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        #3 lists of same line
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        #result
        res=[]
        #check word one by one
        for word in words:
            t=set(word.lower())
            if t<=a or t<=b or t<=c:
                res.append(word)
        return res
                