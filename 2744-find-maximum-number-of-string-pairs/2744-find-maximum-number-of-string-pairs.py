class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[j] == words[i][::-1]:
                    ans += 1
        return ans