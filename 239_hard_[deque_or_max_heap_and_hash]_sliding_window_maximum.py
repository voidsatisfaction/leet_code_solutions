from heapq import heappush, heappop
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        heap = []

        for i in range(k):
            num = nums[i]

            if num in cache:
                cache[num]['count'] += 1
            else:
                num_info = {'num': num, 'count': 1}
                cache[num] = num_info
                heappush(heap, (-num, num_info))

        answer = []

        i,j = -1,k-1
        while True:
            (top_num, top_num_info) = heappop(heap)
            answer.append(-top_num)
            heappush(heap, (top_num, top_num_info))

            i += 1
            j += 1

            if j>=len(nums):
                break

            left_num = nums[i]
            right_num = nums[j]

            if left_num in cache:
                left_num_info = cache[left_num]
                left_num_info['count'] -= 1

            if right_num not in cache:
                right_num_info = {'num': right_num, 'count': 0}
                heappush(heap, (-right_num, right_num_info))
            else:
                right_num_info = cache[right_num]

            right_num_info['count'] += 1
            cache[right_num] = right_num_info

            (top_num, top_num_info) = heappop(heap)
            while top_num_info['count'] == 0:
                del cache[-top_num]
                (top_num, top_num_info) = heappop(heap)
            heappush(heap, (top_num, top_num_info))

        return answer

if __name__ == '__main__':
    assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert Solution().maxSlidingWindow([1], 1) == [1]
    assert Solution().maxSlidingWindow([1, -2], 1) == [1, -2]
    assert Solution().maxSlidingWindow([5, 3, 4, 2, 7], 1) == [5, 3, 4, 2, 7]
    assert Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]



