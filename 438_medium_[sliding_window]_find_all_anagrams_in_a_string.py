from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def is_anagram(state, c_num, c_set):
            for c in c_set:
                if state[c] != c_num[c]:
                    return False
            return True

        if len(s) < len(p):
            return []

        c_set = set()
        c_num = defaultdict(int)
        answer = []

        for c in p:
            c_set.add(c)
            c_num[c] += 1
        
        state = defaultdict(int)
        for i in range(len(p)):
            state[s[i]] += 1

        if is_anagram(state, c_num, c_set):
            answer.append(0)

        for i in range(1, len(s)-len(p)+1):
            j = i+len(p)-1

            state[s[i-1]] -= 1
            state[s[j]] += 1

            if is_anagram(state, c_num, c_set):
                answer.append(i)

        return answer

if __name__ == '__main__':
    print(Solution().findAnagrams('cbaebabacd', 'abc'))
    print(Solution().findAnagrams('abab', 'ab'))