class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i in nums1:
            if i[0] not in d:
                d[i[0]] = i[1]

        for i in nums2:
            if i[0] in d:
                d[i[0]] += i[1]
            else:
                d[i[0]] = i [1]

        ans = []
        for k, v in d.items():
            ans.append([k, v])
        ans.sort()
        return ans

