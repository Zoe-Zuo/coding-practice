class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)==0:
            return b
        if len(b)==0:
            return a
        sum = int (a,2) + int (b,2)
        return bin(sum)[2:]
        