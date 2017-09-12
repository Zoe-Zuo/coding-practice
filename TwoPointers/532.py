class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter=0
        dic={}
        if k>0:
            d=set(nums)
            for i in d:
                if i+k in d:
                    counter+=1
            return counter
        
        elif k==0:
            for i in nums:
                dic[i]=dic.get(i,0)+1
            for i in dic:
                if dic[i]>1:
                    counter+=1
            return counter
        
        else:
            return 0