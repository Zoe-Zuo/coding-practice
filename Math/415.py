class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l=min(len(num1), len(num2))
        res=''
        temp=c=0
        d=len(num1)-len(num2)
        if d>0:
            head=num1[:d]
            num1=num1[d:]
        elif d<0:
            head=num2[:-d]
            num2=num2[-d:]
        else:
            head='0'
        for i in xrange(1, l+1):
            temp=int(num1[-i]) + int(num2[-i]) + c
            if temp >= 10:
                c=1
                res+=str(temp-10)
            else:
                res+=str(temp)
                c=0
        if c==1:
            d=int(head)+1
        else:
            d=int(head)
        if d==0:
            return res[::-1]
        else:
            return str(d)+res[::-1]