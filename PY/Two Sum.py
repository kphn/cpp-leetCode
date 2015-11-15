class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self,nums, target):
        temp={}
        for index in range(len(nums)):
            if target - nums[index] in temp:
                return [temp[target - nums[index]]+1,index + 1]
            temp[nums[index]] = index

