class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        Lists=[]
        for i in range(0,rowIndex+1):
            Lists.append([1]*(i+1))
            if i>1:
                for j in range(1,i):
                    Lists[i][j]=Lists[i-1][j-1]+Lists[i-1][j]
        return Lists[rowIndex]
