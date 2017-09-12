class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=min(nums)
        s=0
        for num in nums:
           d=num-m
           s=d+s
        return s
            