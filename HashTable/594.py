class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=collections.Counter(nums)
        return max([count[i]+count[i+1] for i in count if count[i+1]] or [0])