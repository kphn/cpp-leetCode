from _ast import Add
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add = 1
        for i in reversed(range(len(digits))):
            if digits[i]<9:
                digits[i]+=add
                add=0
                break
            else:
                digits[i] = 0
        if add == 1:
            digits.insert(0,1)
        return digits
    
s = Solution()
print s.plusOne([9,8,8])
                