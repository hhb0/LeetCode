class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and words[j] != words[i]:
                    ans.append(words[i])
                    break
        return ans