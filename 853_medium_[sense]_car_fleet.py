from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_list = zip(position, speed)
        reversed_sorted_position_speed_list = reversed(sorted(position_speed_list, key=lambda x: x[0]))

        answer, current_max_reach_time = 0, 0
        for position, speed in reversed_sorted_position_speed_list:
            distance = target - position
            time = distance / speed

            if time > current_max_reach_time:
                answer += 1
                current_max_reach_time = time

        return answer


if __name__ == '__main__':
    s = Solution()

    assert s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3

    assert s.carFleet(10, [3], [3]) == 1
