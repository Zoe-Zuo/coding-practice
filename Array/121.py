class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res=0
        min=prices[0]
        for nums in prices:
            if nums<min:
                min=nums
            elif nums-min>res:
                res=nums-min
        return res