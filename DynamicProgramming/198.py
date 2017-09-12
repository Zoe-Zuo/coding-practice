class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        for n in nums:
            l, r = r, max(n + l, r)
        return r