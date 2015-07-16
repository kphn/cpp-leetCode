class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self,nums, target):
        temp={}
        for index in range(len(num)):
            if target - num[index] in temp:
                return [temp[target - num[index]]+1,index + 1]
            temp[num[index]] = index

