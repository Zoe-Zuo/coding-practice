class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1=list(enumerate(list1))
        list2=list(enumerate(list2))
        for index, item in list1:
            if item in list2:
                enumerate