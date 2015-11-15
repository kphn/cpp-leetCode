class Solution(object):
    def longestPalindrome(self, s):
        start=0;end=0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            leng = max(len1,len2)
            if(leng > end-start):
                start = i-(leng-1)/2
                end = i+leng/2
        return s[start:end+1]
        
    def expandAroundCenter(self,s,l,r):
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
        return r-l-1
    
so = Solution()
print so.longestPalindrome("abcdcbae")