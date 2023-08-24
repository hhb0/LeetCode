class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if set(nums1) & set(nums2):
            ans = list(set(nums1) & set(nums2))
            ans.sort()
            return ans[0]
        else:
            return -1
        