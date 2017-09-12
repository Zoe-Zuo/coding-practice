class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        count=[0]*(l+1)
        for x in nums:
            count[x]+=1
        for x in xrange(1, l+1):
            if count[x]==2:
                twice=x
            if count[x]==0:
                never=x
        return twice, never
            
                