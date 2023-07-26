class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c1 = Counter()
        c1_cnt = 0
        c2 = Counter(nums)
        c2_cnt = len(nums)
        dominant = c2.most_common()[0][0]

        ans = -1
        for i in range(len(nums)):
            c1[nums[i]] += 1
            c1_cnt += 1
            c2[nums[i]] -= 1
            c2_cnt -= 1
            # dominant가 각각의 subarray에서도 dominant인지 검사
            if nums[i] == dominant:
                if c1[nums[i]] * 2 > c1_cnt and c2[nums[i]] * 2 > c2_cnt:
                    ans = i
                    break
        return ans