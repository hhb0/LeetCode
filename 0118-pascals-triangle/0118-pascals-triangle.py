class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        dp = [1]
        answer.append(dp)
        for i in range(1, numRows):
            new_dp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    new_dp.append(1)
                else:
                    new_dp.append(dp[j-1] + dp[j])
            answer.append(new_dp)
            dp = new_dp
        return answer
