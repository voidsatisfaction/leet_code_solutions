from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def remove_and_return_new_list(nums: List[int], val: int) -> List[int]:
            new_list = []
            for num in nums:
                if num == val:
                    continue
                new_list.append(num)

            return new_list
        def permute_recursive(nums: List[int]) -> List[List[int]]:
            if len(nums) == 1:
                return [nums]

            permutations = []
            for num in nums:
                altered_nums = remove_and_return_new_list(nums, num)
                for per in permute_recursive(altered_nums):
                    permutations.append([num] + per)

            return permutations

        if len(nums) == 0:
            return [[]]

        return permute_recursive(nums)

class Solution:
    def backtrack(self, nums, used_nums_set, state, answer) -> None:
        if len(nums) == len(state):
            answer.append(state)
            return

        for num in nums:
            if num in used_nums_set:
                continue
            
            used_nums_set.add(num)

            self.backtrack(nums, used_nums_set, state + [num], answer)

            used_nums_set.remove(num)

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        answer = []
        self.backtrack(nums, set(), [], answer)

        return answer

if __name__ == '__main__':
    print(Solution().permute([1]))
    print(Solution().permute([1,2]))
    print(Solution().permute([1,2,3]))