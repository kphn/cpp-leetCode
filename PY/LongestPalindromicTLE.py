from __builtin__ import str
class Solution(object):
    def longestPalindrome(self,s):
        palindrome = ""
        for i in range(len(s)):
            len1 = len(self.expandFromCenter(s, i, i))
            if len1 > len(palindrome):
                palindrome = self.expandFromCenter(s, i, i)
            len2 = len(self.expandFromCenter(s, i, i+1))
            if len2>len(palindrome):
                palindrome = self.expandFromCenter(s, i, i+1)
        return palindrome
    def expandFromCenter(self,s,l,r):
        while l>= 0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]

s = Solution()
print s.longestPalindrome("abcdeedcba")