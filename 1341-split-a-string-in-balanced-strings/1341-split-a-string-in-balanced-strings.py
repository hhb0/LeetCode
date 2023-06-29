class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R_L_count = {'R':0,"L":0}
        max_balanced = 0

        for index in range(len(s)):

            R_L_count[s[index]] +=1

            # they are equal means, they are balanced
            if R_L_count["R"] == R_L_count["L"]:

                max_balanced +=1

        return max_balanced