class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque

        src_color = image[sr][sc]
        q = deque([(sr, sc)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        while q:
            cur_y, cur_x = q.popleft()
            if (cur_y, cur_x) in visited:
                continue
            visited.add((cur_y, cur_x))
            image[cur_y][cur_x] = color

            for direction in directions:
                new_y = cur_y + direction[0]
                new_x = cur_x + direction[1]
                if new_y < 0 or new_y > len(image) -1:
                    continue
                if new_x < 0 or new_x > len(image[0]) -1:
                    continue
                if image[new_y][new_x] == src_color:
                    q.append((new_y, new_x))

        return image