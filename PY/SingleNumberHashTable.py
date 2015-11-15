class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] = 2
        for i in a:
            if a[i] == 1:
                return i
    
s = Solution()
print s.singleNumber([1,1,2,3,2,4,5,4,5])