class Solution:
    def maxScore(self, s: str) -> int:
        ans = []
        
        for i in range(1, len(s)):
            l = s[:i].count("0")
            r = s[i:].count("1")
            ans.append(l+r)

        return max(ans)
