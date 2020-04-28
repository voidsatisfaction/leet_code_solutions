from typing import List

INF = 1987654321

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals

        intervals.sort(key=lambda interval: interval[0])
        merged_interval = intervals[0]
        answer = []

        for interval in intervals:
            front, rear = interval[0], interval[1]
            [_, current_max_rear_num] = merged_interval

            if front <= current_max_rear_num:
                if current_max_rear_num < rear:
                    merged_interval[1] = rear
            else:
                answer.append(merged_interval)
                merged_interval = interval

        answer.append(merged_interval)

        return answer
                

if __name__ == '__main__':
    print(Solution().merge([[15,18], [1,3],[2,6],[8,10]]))
    print(Solution().merge([[1,4],[4,5]]))
    print(Solution().merge([[4,5]]))