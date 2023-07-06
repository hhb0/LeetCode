class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h = {}
        for i in range(len(names)):
            h[heights[i]] = names[i]

        h_sort = sorted(h.items(), reverse = True)

        ans = []
        for height, name in h_sort:
            ans.append(name)

        return ans
        