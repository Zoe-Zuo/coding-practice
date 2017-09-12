class Solution(object):
    def subsets(self, set):
        """
        :type set: List[int]
        :rtype: List[List[int]]
        """
        if len(set)==0:
            return [[]]
        smaller = self.subsets(set[:-1])
        extra = set[-1:]
        new = []
        for small in smaller:
            new.append (small + extra)
        return smaller + new        