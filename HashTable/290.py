class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #split string
        l=str.split(' ')
        #compare string length and pattern length
        if len(pattern) != len(l):
            return False
        return map(pattern.find, pattern)==map(l.index, l)