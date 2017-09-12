class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in s:
            dic[i]=dic.get(i,0)+1
        for j in t:
            if j in dic:
                if dic[j]==0:
                    return j
                else:
                    dic[j]-=1
            else:
                return j
                
                