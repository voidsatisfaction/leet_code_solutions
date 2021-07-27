from typing import List
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        DIV = 60

        num_set, counter = set(), defaultdict(int)
        for num in time:
            num_set.add(num % DIV)
            counter[num % DIV] += 1
        
        answer = 0
        for num in num_set:
            if num == 0 or num == DIV//2:
                answer += counter[num] * (counter[num]-1) // 2
            if num > 0 and num < DIV//2:
                answer += counter[num] * counter[DIV-num]

        return answer

if __name__ == '__main__':
    s = Solution()

    assert s.numPairsDivisibleBy60([30,20,150,100,40]) == 3

    assert s.numPairsDivisibleBy60([60,60,60]) == 3

    assert s.numPairsDivisibleBy60([60]) == 0

    assert s.numPairsDivisibleBy60([30]) == 0
