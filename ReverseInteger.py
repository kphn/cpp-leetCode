class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        type =1
        if x<0:
            type=-1
        x = abs(x)
        res = []
        while(x>0):
            if x%10 == 0:
                if len(res)==0:
                    x/=10
                    continue
            res.append(x%10)
            x/=10
        re=0
        for i in res:
            re = re*10+i
        return re*type
    
s = Solution()
print s.reverse(-1012)