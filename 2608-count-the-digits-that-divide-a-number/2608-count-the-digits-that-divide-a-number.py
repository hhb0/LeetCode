class Solution:
    def countDigits(self, num: int) -> int:
        c = 0

        for v in str(num):
            if num % int(v) == 0:
                c += 1
        
        return c