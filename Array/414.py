class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m0=m1=m2 = -1*sys.maxint
        for i in nums:
            if i >=m0:
                if i!=m0:
                    m2=m1
                    m1=m0
                    m0=i
            elif i>=m1:
                if i!=m1:
                    m2=m1
                    m1=i
            elif i>m2:
                if i!=m2:
                    m2=i
        return m0 if m2==-1*sys.maxint else m2
                
        