from itertools import combinations
class Solution:
    def subsetSums(self, arr):
        sums_list = []
        n = len(arr)
        for r in range(n+1):
            for subset in combinations(arr,r):
                sums_list.append(sum(subset))
        return sums_list

arr = [2,3,4,5]
solution = Solution()
x = solution.subsetSums(arr)
print(x)