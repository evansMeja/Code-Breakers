class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m - 1+ n - 1 , m - 1)
