class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        prev = 1
        for i in range(1, len(s)):
            diff = ord(s[i]) - ord(s[i-1])
            # diff가 1일 때, prev 값을 1 더해줌. 이는 연속한다는 의미
            if diff == 1:
                prev += 1
                ans = max(ans, prev) 
            # diff가 1이 아닐 때는 연속이 끊긴 상태이니 prev 값을 1로 재설정
            else:
                prev = 1
                ans = max(ans, prev)
        return ans