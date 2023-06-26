class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        arr_cnt = Counter(arr)
        arr_v = arr_cnt.values()

        return len(arr_v) == len(set(arr_v))
