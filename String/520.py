class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        list=[]
        if ord (word[0])>=97:
            for i in word[1:]:
                if ord(i)<=90:
                    return False
            return True
        if ord(word[0])<=90:
            for i in word[1:]:
                if ord(word[1]) <=90:
                    if ord(i)>=97:
                        return False
                if ord(word[1]) >=97:
                    if ord(i)<=90:
                        return False
            return True
            
                
            