from typing import List, Tuple
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self._key_to_time_value_list = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self._key_to_time_value_list[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        time_value_list = self._key_to_time_value_list[key]

        answer = self._binary_search(timestamp, time_value_list)

        return answer

    def _binary_search(self, timestamp: int, time_value_list: List[Tuple[int, str]]) -> str:
        if len(time_value_list) == 0:
            return ''

        left, right = 0, len(time_value_list)

        while left < right:
            mid = (left + right) // 2

            time, value = time_value_list[mid]

            if timestamp >= time:
                left = mid+1
            elif timestamp < time:
                right = mid

        return '' if left == 0 else time_value_list[left-1][1]


if __name__ == '__main__':
    timeMap = TimeMap();
    timeMap.set("foo", "bar", 1)
    assert timeMap.get("foo", 1) == 'bar'
    assert timeMap.get("foo", 3) == 'bar'
    timeMap.set("foo", "bar2", 4)
    assert timeMap.get("foo", 4) == 'bar2'
    assert timeMap.get("foo", 5) == 'bar2'