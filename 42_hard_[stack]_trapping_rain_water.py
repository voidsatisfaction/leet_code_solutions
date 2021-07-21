from typing import List
from collections import namedtuple

Wall = namedtuple('Wall', ['index', 'height'])

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        answer = 0

        for index, h in enumerate(height):
            if len(stack) == 0 and height == 0:
                continue
            
            previous_top_height = 0
            while len(stack)>0 and h >= stack[-1].height:
                stack_top = stack.pop()
                answer += (index - stack_top.index - 1) * (stack_top.height - previous_top_height)

                previous_top_height = stack_top.height
            
            if len(stack) > 0 and stack[-1].height >= h and previous_top_height < h:
                answer += (h - previous_top_height) * (index - stack[-1].index - 1)

            stack.append(Wall(index=index, height=h))

        return answer

if __name__ == '__main__':
    s = Solution()

    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

    assert s.trap([4,2,0,3,2,5]) == 9