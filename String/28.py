class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        for index in range(0,len(haystack)):
            if needle==haystack[index:index+len(needle)]:
                return index
        return -1
        