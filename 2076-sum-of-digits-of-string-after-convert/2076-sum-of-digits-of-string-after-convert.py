class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted_num = "".join([str(ord(n)-96) for n in s])
        
        while(k):
            ans = 0
            for n in converted_num:
                ans += int(n)

            converted_num = str(ans)
            k -= 1
        return ans

        