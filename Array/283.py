class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p=0
        for i in xrange(len(nums)):
            if nums[i]!=0:
                nums[i], nums[p]=nums[p],nums[i]
                p+=1