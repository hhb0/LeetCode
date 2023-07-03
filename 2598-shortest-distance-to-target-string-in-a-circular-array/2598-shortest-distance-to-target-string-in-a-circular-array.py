class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        for i in range(n):
            l = words[(startIndex - i) % n]
            r = words[(startIndex + i) % n]
            if target == l or target == r:
                return i

        return -1