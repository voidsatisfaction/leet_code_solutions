from typing import List

class Solution:
    def _dfs(self, digits, depth, candidate, digit_to_alphabet_list, answer):
        if depth == len(digits):
            answer.append(candidate)
            return

        current_digit = digits[depth]

        for alphabet in digit_to_alphabet_list[current_digit]:
            self._dfs(digits, depth+1, candidate+alphabet, digit_to_alphabet_list, answer)

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        digit_to_alphabet_list = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        answer = []

        self._dfs(digits, 0, '', digit_to_alphabet_list, answer)

        return answer

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

        res = ['']
        for d in digits:
            new_res = []
            for pre in res:
                for cur in MAPPING[int(d)]:
                    new_res.append(pre + cur)

            res = new_res

        if len(digits) == 0:
            return []

        return res

if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
    print(Solution().letterCombinations(''))