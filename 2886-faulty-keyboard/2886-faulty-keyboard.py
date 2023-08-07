class Solution:
    def finalString(self, s: str) -> str:
        result = ''

        for text in s.split('i'):
            result = result[::-1] + text

        return result