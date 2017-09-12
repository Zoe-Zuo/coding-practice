class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic_1={}
        dic_2={}
        res=[]
        for a in nums1:
            dic_1[a]=dic_1.get(a,0)+1
        for b in nums2:
            if b in dic_1 and dic_1[b]>0:
                    res.append(b)
                    dic_1[b]-=1
        return res