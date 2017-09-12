class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for i in magazine:
            dic[i]=dic.get(i,0)+1
        for j in ransomNote:
            if j in dic:
                if dic[j]==0:
                    return False
                else:
                    dic[j]-=1
            if j not in dic:
                return False
        return True
                