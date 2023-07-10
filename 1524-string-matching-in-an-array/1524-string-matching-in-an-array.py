class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)

        ans = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[j].find(words[i]) >= 0:
                    ans.append(words[i])
                    break
        return ans