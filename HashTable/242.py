class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s={}
        dic_t={}
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        else:
            for a in s:
                if a not in dic_s:
                    dic_s[a]=1
                else:
                    dic_s[a]+=1
            for b in t:
                if b not in dic_t:
                    dic_t[b]=1
                else:
                    dic_t[b]+=1
            return dic_s==dic_t
                        