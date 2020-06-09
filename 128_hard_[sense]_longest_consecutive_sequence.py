from collections import deque
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def bfs(num, cache) -> int:
            count = 1
            q = deque()

            q.appendleft(num)
            while q:
                n = q.popleft()
                cache[n] = True

                if (n+1) in cache and cache[n+1] is False:
                    q.append(n+1)
                    count += 1

                if (n-1) in cache and cache[n-1] is False:
                    q.append(n-1)
                    count += 1

            return count

        max_count = 0
        cache = {}

        for num in nums:
            cache[num] = False

        for num in nums:
            if cache[num] is False:
                max_count = max(max_count, bfs(num, cache))

        return max_count

if __name__ == '__main__':
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([]) == 0
    assert Solution().longestConsecutive([100]) == 1
    assert Solution().longestConsecutive([100, 100]) == 1