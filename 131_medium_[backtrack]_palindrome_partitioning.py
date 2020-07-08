from typing import List, DefaultDict, Set

from collections import defaultdict

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []

        if len(s) == 1:
            return [[s]]

        adjList = defaultdict(set)

        palindrome_node_candidate_set = set()

        for i in range(len(s)):
            palindrome_node_candidate_set.add((i, i))
            adjList[i].add((i+1, s[i]))
            if i == len(s)-1:
                break

            if s[i] == s[i+1]:
                palindrome_node_candidate_set.add((i, i+1))
                adjList[i].add((i+2, s[i:i+2]))

        while len(palindrome_node_candidate_set) > 0:
            start_index, end_index = palindrome_node_candidate_set.pop()

            next_start_index = start_index-1
            next_end_index = end_index+1

            if next_start_index < 0 or next_end_index > len(s)-1:
                continue

            if s[next_start_index] == s[next_end_index]:
                palindrome_node_candidate_set.add((next_start_index, next_end_index))
                adjList[next_start_index].add((next_end_index+1, s[next_start_index:next_end_index+1]))

        def dfs(node_num: int, cache: List[str], adjList, answer: List[List[str]]) -> None:
            if node_num == len(s):
                answer.append(cache[:])
                return

            for (next_index, palindrome) in adjList[node_num]:
                cache.append(palindrome)

                dfs(next_index, cache, adjList, answer)

                cache.pop()

        answer = []

        dfs(0, [], adjList, answer)

        return answer

            

            

if __name__ == '__main__':
    s = Solution()

    print(s.partition('aab'))
    print(s.partition('efe'))