class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one=nums[:]
        two=nums[:]
        for i in xrange(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                one[i]=nums[i+1]
                two[i+1]=nums[i]
                break
        def val(arr):
            for i in xrange(0,len(arr)-1):
                if arr[i]>arr[i+1]:
                    return False
            return True
        return val(one) or val(two)
            