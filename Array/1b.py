class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(0,len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if nums[j]==target-nums[i]:
                    return [i,j]