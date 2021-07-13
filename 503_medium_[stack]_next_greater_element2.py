from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, answer = [], [ 0 for _ in range(len(nums)) ]

        for _ in range(2):
            for i in range(len(nums)-1, -1, -1):
                while len(stack)>0 and nums[i] >= nums[stack[-1]]:
                    stack.pop()

                if len(stack) == 0:
                    answer[i] = -1
                    stack.append(i)
                else:
                    answer[i] = nums[stack[-1]]
                    stack.append(i)

        return answer

        
if __name__ == '__main__':
    s = Solution()

    assert s.nextGreaterElements([1, 2, 1]) == [2, -1, 2]
    assert s.nextGreaterElements([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
