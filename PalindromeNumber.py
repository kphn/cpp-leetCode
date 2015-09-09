class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:return False
        div = 1
        while div*10<=x:
            div*=10
        while div>1:
            if x/div != x%10:
                return False
            x%=div
            div/=100
            x/=10
        return True

s = Solution()
print s.isPalindrome(12343211)