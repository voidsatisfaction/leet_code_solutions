from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_cache = defaultdict(list)
        for s in strs:
            cache = defaultdict(int)
            for c in s:
                cache[c] += 1

            group_cache_key = ''
            for key in sorted(list(cache.keys())):
                value = cache[key]
                group_cache_key += f'{key}{value}'

            group_cache[group_cache_key].append(s)

        return list(group_cache.values())

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
