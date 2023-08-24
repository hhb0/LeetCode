class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    # 왼쪽 칸에서 오른쪽 칸으로 이동하는 방법 밖에 없음
                    grid[i][j] += grid[i][j-1]

                elif j == 0:
                    # 위 칸에서 아래로 이동하는 방법 밖에 없음
                    grid[i][j] += grid[i-1][j]

                else:
                    # 위에서 내려오거나 왼쪽에서 오른쪽으로 이동하거나
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]

        return grid[-1][-1]