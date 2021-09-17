from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours_to_eat(piles: List[int], k: int) -> int:
            hours = 0
            for pile in piles:
                hours += (pile // k)
                if pile % k > 0:
                    hours += 1

            return hours

        left, right = 1, 10**9+1
        while left < right:
            mid = (left + right) // 2
            if get_hours_to_eat(piles, mid) > h:
                left = mid + 1
            else:
                right = mid

        return left

if __name__ == '__main__':
    s = Solution()

    assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4

    assert s.minEatingSpeed([30,11,23,4,20], 5) == 30

    assert s.minEatingSpeed([30,11,23,4,20], 6) == 23