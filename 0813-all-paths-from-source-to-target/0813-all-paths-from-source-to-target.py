class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque

        total_path = []
        q = deque([(0, [])])

        while q:
            cur_node, cur_path = q.popleft()

            if cur_node == len(graph) -1:
                total_path.append(cur_path + [cur_node])
            for node in graph[cur_node]:
                q.append((node, cur_path + [cur_node]))

        return total_path
