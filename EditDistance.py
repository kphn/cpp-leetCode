class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        dp = [[0 for col in range(len(word1))] for row in range(len(word2))]
        for i in range(len(word1)):
            if word2[0] in word1[0:i+1]:
                dp[0][i] = i
            else:
                dp[0][i] = i+1
        for i in range(len(word2)):
            if word1[0] in word2[0:i+1]:
                dp[i][0] = i
            else:
                dp[i][0] = i+1
        
        for i in range(1,len(word2)):
            for j in range(1,len(word1)):
                diff = 0
                if word2[i]!=word1[j]:
                    diff =1
                
                dp[i][j] = min(dp[i][j-1]+1 , dp[i-1][j]+1 , dp[i-1][j-1]+diff)
        
        return dp[len(word2)-1][len(word1)-1]
        
s = Solution()
print s.minDistance("1234", "234")
