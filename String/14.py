class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        length = len(strs[0])
        index = 0
        for i in range(0, len(strs)):
            if len(strs[i])<length:
                length = len(strs[i])
                index = i
                
        for j in range(0,length):
            for i in range(0,len(strs)):
                if strs[0][j]!=strs[i][j]:
                    lcp=strs[0][0:j]
                    return lcp
        return strs[index]     
            
            
                