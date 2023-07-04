class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cum_sum = []
        prev = 0
        ans = 1

        for num in nums:
            prev += num
            cum_sum.append(prev)
        if min(cum_sum) < 0:
            return 1 -(min(cum_sum))
            

        return ans
