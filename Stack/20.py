class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dic={'(':')', '[':']', '{':'}'}
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in dic.keys():
                stack.append(i)
            if i in dic.values():
                if stack and dic[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return not stack