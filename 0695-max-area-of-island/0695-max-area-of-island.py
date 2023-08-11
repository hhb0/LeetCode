class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque

        answer = 0
        visited = set()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if (i, j) in visited:
                    continue

                if grid[i][j] == 0:
                    continue

                q = deque([(i, j)])
                area = 0
                while q:
                    cur_y, cur_x = q.popleft()
                    if (cur_y, cur_x) in visited:
                        continue
                    visited.add((cur_y, cur_x))

                    area += 1
                    for move in moves:
                        new_y = cur_y + move[0]
                        new_x = cur_x + move[1]
                        if new_y < 0 or new_y > len(grid) - 1:
                            continue
                        if new_x < 0 or new_x > len(grid[0]) - 1:
                            continue
                        if grid[new_y][new_x] == 1:
                            q.append((new_y, new_x))

                answer = max(area, answer)
        return answer
                        