import heapq
from typing import List, Tuple

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        def heappush_based_on_processing_time(heap, task_with_index) -> None:
            heapq.heappush(heap, (task_with_index[1], task_with_index[2]))

        def heappop(heap) -> Tuple[int, int]:
            return heapq.heappop(heap)

        task_with_index_list = [ (task[0], task[1], index) for index, task in enumerate(tasks) ]
        sorted_task_with_index_list = list(reversed(sorted(task_with_index_list)))
        
        first_task_with_index = sorted_task_with_index_list.pop()
        current_time = first_task_with_index[0]

        min_processing_time_heap = []
        heappush_based_on_processing_time(min_processing_time_heap, first_task_with_index)

        answer = []
        while len(sorted_task_with_index_list) > 0 or len(min_processing_time_heap) > 0:
            if len(min_processing_time_heap) > 0:
                processing_time, index = heappop(min_processing_time_heap)

                answer.append(index)
                current_time += processing_time

                while len(sorted_task_with_index_list) > 0 and sorted_task_with_index_list[-1][0] <= current_time:
                    heappush_based_on_processing_time(min_processing_time_heap, sorted_task_with_index_list.pop())
            else:
                current_time = sorted_task_with_index_list[-1][0]
                heappush_based_on_processing_time(min_processing_time_heap, sorted_task_with_index_list.pop())

        return answer



if __name__ == '__main__':
    s = Solution()

    assert s.getOrder([[1,2],[2,4],[3,2],[4,1]]) == [0,2,3,1]

    assert s.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]) == [4,3,2,0,1]

    assert s.getOrder([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]) == [5,0,1,3,2,4]
