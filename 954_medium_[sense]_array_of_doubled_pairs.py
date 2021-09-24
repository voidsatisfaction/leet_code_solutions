from collections import defaultdict
from typing import List, DefaultDict

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        def is_valid_arr(arr: List[int], integer_to_count_map: DefaultDict[int, int]) -> bool:
            if len(arr) == 0:
                return True

            for n in arr:
                integer_to_count_map[2*n] -= integer_to_count_map[n]
                integer_to_count_map[n] = 0

                if integer_to_count_map[2*n] < 0:
                    return False

            return integer_to_count_map[arr[-1]] == 0

        integer_to_count_map = defaultdict(int)

        for n in arr:
            integer_to_count_map[n] += 1

        if integer_to_count_map[0] % 2 != 0:
            return False
        
        sorted_negative_arr = sorted([n for n in arr if n < 0], reverse=True)
        sorted_positive_arr = sorted([n for n in arr if n > 0])

        return is_valid_arr(sorted_negative_arr, integer_to_count_map) and \
            is_valid_arr(sorted_positive_arr, integer_to_count_map)


if __name__ == '__main__':
    s = Solution()

    assert s.canReorderDoubled([3,1,3,6]) is False

    assert s.canReorderDoubled([2,1,2,6]) is False

    assert s.canReorderDoubled([4,-2,2,-4]) is True

    assert s.canReorderDoubled([1,2,4,16,8,4]) is False
