class Solution:
    def countDigits(self, num: int) -> int:
        digits = []

        for v in str(num):
            if num % int(v) == 0:
                digits.append(v)
        
        return len(digits)