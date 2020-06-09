from typing import List
from queue import Queue
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_name_to_task_data = {}
        for task_name in tasks:
            if task_name not in task_name_to_task_data:
                # task_data => (count, name, cooling_count)
                task_name_to_task_data[task_name] = (-1, task_name, 0)
            else:
                task_data = task_name_to_task_data[task_name]
                task_name_to_task_data[task_name] = (task_data[0]-1, task_name, 0)

        min_heap = []
        for task_name in task_name_to_task_data.keys():
            heappush(min_heap, task_name_to_task_data[task_name])

        cooling_task_data_list = []
        answer = 0

        while len(min_heap) > 0 or len(cooling_task_data_list) > 0:
            new_cooling_task_data_list = []

            if len(min_heap) > 0:
                (count, name, cooling_count) = heappop(min_heap)
                count += 1
                if count < 0 and n == 0:
                    heappush(min_heap, (count, name, cooling_count))
                elif count < 0:
                    new_cooling_task_data_list.append((count, name, n))
                else:
                    pass
            
            for cooling_task_data in cooling_task_data_list:
                (count, name, cooling_count) = cooling_task_data
                cooling_count -= 1

                if cooling_count == 0:
                    heappush(min_heap, (count, name, cooling_count))
                else:
                    new_cooling_task_data_list.append((count, name, cooling_count))

            cooling_task_data_list = new_cooling_task_data_list

            answer += 1

        return answer

if __name__ == '__main__':
    assert Solution().leastInterval(["A","A","A","B","B","B"], 2) == 8
    assert Solution().leastInterval(["A"], 0) == 1
    assert Solution().leastInterval(["A", "A"], 1) == 3