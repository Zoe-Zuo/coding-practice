class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=len(nums)-1
        l=sorted(nums)
        for i in xrange(0, len(nums)):
            if l[i]!=nums[i]:
                start=i
                break
        while end>=0:
            if l[end]!=nums[end]:
                end=end
                break
            else:
                end-=1
        return end-start+1