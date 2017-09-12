class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        try:
            insert=nums.index(target)
            return insert
        except:
            insert=0
            for i in range (0,len(nums)):
                if target>nums[i]:
                    insert=insert+1
                else:
                    return insert
            return insert
                