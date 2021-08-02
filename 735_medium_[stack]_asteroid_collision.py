from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
            elif stack[-1] > 0 and asteroid < 0:
                stack.append(asteroid)
                while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                    top = stack.pop()
                    next_top = stack.pop()

                    if abs(top) > abs(next_top):
                        stack.append(top)
                    elif abs(top) < abs(next_top):
                        stack.append(next_top)
            else:
                stack.append(asteroid)

        return stack


if __name__ == '__main__':
    s = Solution()

    assert s.asteroidCollision([5, 10, -5]) == [5, 10]

    assert s.asteroidCollision([8, -8]) == []

    assert s.asteroidCollision([10, 2, -5]) == [10]

    assert s.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]