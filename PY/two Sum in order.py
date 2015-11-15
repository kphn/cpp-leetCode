#two sum nums sorted
class Solution:
	'''利用二分法来寻找排序后的数值'''
	def bSearch(nums,target,start):
		L = start;R = len(nums)-1
		while(L<R):
			M = (L+R)/2
			if(nums[M] < target):
				L = M+1
			else:
				R=M
		if(L==R && nums[L]==target):
			return L
		else:
			return -1
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self,nums, target):
    	'''利用二分法来寻找数值'''
    	for i in range(len(nums)):
    		if(self.bSearch(nums,target-nums[i],i+1) != -1):
    			return [i+1,self.bSearch(nums,target-nums[i],i+1)+1]


class Solution1:
	'''利用两个指针来实现O(n)复杂度的寻找，分为左右两个指针i，j
	i初始为0，j初始为数组的最大值
	如果A[i]+A[j]>target; 增加i无用，因此我们减少j
	如果A[i]+A[j]<target;减少j并没有用，因此我们增加i
	如果A[i]+A[j]=target;则找到结果
	'''
	def twoSum(self,nums, target):
		i = 0;j=len(nums)-1
		while(i<j):
			sum = nums[i] + nums[j]
			if (sum<target):
				i+=1
			else if(sum>target):
				j-=1
			else:
				return [i+1,j+1]
