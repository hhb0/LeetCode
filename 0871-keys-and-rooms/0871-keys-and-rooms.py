class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque

        ans = False
        q = deque([0])
        visited = set()

        while q:
            room = q.popleft()
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    q.append(key)

            if len(visited) == len(rooms):
                ans = True
                break

        return ans