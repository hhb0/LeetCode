class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]
        for i in range(3, n+1):
            dp.append(sum(dp[i-3:i]))
        return dp[-1]