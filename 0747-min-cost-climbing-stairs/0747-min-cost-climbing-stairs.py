class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        n = len(cost)
        
        if n < 2:
            return dp[n]

        for i in range(2, n+1):
            dp.append(min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]))

        return dp[-1]

