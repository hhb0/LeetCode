class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if( nums[i]+nums[j]<target):
                    ans+=1
        return ans