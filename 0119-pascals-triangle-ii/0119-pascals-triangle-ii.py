class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        for i in range(1, rowIndex + 1):
            new_dp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    new_dp.append(1)
                else:
                    new_dp.append(dp[j-1] + dp[j])
            dp = new_dp
        return dp