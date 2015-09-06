class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        
        return res

s = Solution()
print s.singleNumber([1,1,2,2,3,4,5,4,5])
