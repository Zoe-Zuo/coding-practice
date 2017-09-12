class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        temp=res=0
        min=prices[0]
        for i in range(0,len(prices)):
            if prices[i]>min:
                temp=prices[i]-min
                res=temp+res
                try: 
                    min=prices[i+1]
                except:
                    break
            if prices[i]<min:
                min=prices[i]
        return res