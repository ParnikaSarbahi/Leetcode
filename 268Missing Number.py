class Solution(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1))-sum(nums)
''' 
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(0,len(nums)):
            if(i!=nums[i]):
                return i
            if(len(nums) not in nums):
                return len(nums)

class Solution(object):
    def missingNumber(self, nums):
        for i in range(0,len(nums)+1):
            if(i not in nums):
                return i
'''
               
        
