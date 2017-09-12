class Solution(object):
    def singleNumber(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=A[0]
        for i in xrange(1, len(A)):
            res=res^A[i]
        return res