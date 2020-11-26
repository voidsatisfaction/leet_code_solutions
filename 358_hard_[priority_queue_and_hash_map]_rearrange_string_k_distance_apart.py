import heapq
from collections import defaultdict

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0 or k == 1:
            return s

        ans = ''
        cooltime_zero_count_max_heap = []

        char_to_count = defaultdict(int)
        for c in s:
            char_to_count[c] += 1

        for c in char_to_count:
            c_count = char_to_count[c]
            heapq.heappush(cooltime_zero_count_max_heap, (-c_count, c))

        cooltime_not_zero_c_to_cooltime_map = {}

        while len(cooltime_zero_count_max_heap) > 0:
            _, c = heapq.heappop(cooltime_zero_count_max_heap)

            char_to_count[c] -= 1
            ans += c

            if char_to_count[c] > 0:
                cooltime_not_zero_c_to_cooltime_map[c] = k

            char_list_to_delete = []
            for cooltime_not_zero_c in cooltime_not_zero_c_to_cooltime_map:
                cooltime_not_zero_c_to_cooltime_map[cooltime_not_zero_c] -= 1

                if cooltime_not_zero_c_to_cooltime_map[cooltime_not_zero_c] == 0:
                    char_list_to_delete.append(cooltime_not_zero_c)

                    heapq.heappush(
                        cooltime_zero_count_max_heap,
                        (-char_to_count[cooltime_not_zero_c], cooltime_not_zero_c)
                    )

            for char_to_delete in char_list_to_delete:
                del cooltime_not_zero_c_to_cooltime_map[char_to_delete]

        if len(ans) != len(s):
            return ''

        return ans


if __name__ == '__main__':
    s = Solution()

    assert s.rearrangeString('aabbcc', 3) != ''
    assert s.rearrangeString('aaabc', 3) == ''
    assert s.rearrangeString('aaadbbcc', 2) != ''
    assert s.rearrangeString('skdlfmldsmfls', 1) != ''