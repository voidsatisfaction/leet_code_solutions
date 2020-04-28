from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m-1+n-1, m-1)

if __name__ == '__main__':
    print(Solution().uniquePaths(3, 2))