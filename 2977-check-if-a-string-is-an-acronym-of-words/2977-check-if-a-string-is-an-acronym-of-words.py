class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans = False
        w = ""

        for word in words:
            w+=word[0]

        if w == s:
            ans = True

        return ans