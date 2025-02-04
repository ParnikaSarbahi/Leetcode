class Solution(object):
    def longestMonotonicSubarray(self, nums):
        c1=1
        c=1
        for i in range(len(nums)-1):
            if(nums[i]<nums[i+1]):
                c1+=1
                if(c<c1):
                    c=c1
            else:
                c1=1
        p1=1
        p=1
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                p1+=1
                if(p<p1):
                    p=p1
            else:
                p1=1
        return(max(p,c))
