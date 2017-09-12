class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum=0.0
        for i in xrange(0,k):
            sum+=nums[i]
        max=sum
        for i in xrange(k,len(nums)):
            sum=sum+nums[i]-nums[i-k]
            if sum >max:
                max=sum
        return max/k