class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k==0:
            return False
        dic={}
        for i in xrange (0,len(nums)):
            if nums[i] not in dic:
                dic [nums[i]]=i
            else: 
                d = i - dic[nums[i]]
                dic[nums[i]]=i
                if d<=k:
                    return True
        return False
                    
                