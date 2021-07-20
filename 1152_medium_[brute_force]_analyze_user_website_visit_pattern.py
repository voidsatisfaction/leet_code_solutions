from typing import List
from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        timestamp_username_website_list = list(sorted(zip(timestamp, username, website)))

        sorted_username_to_website_map = defaultdict(list)
        for _, user, word in timestamp_username_website_list:
            sorted_username_to_website_map[user].append(word)

        combination_counter = defaultdict(int)
        for website_list in sorted_username_to_website_map.values():
            for combination in set(combinations(website_list, 3)):
                combination_counter[combination] += 1

        sorted_combination_counter = sorted(combination_counter.keys(), key=lambda x: (-combination_counter[x], x))

        return list(sorted_combination_counter[0])

if __name__ == '__main__':
    s = Solution()

    assert s.mostVisitedPattern(
        ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
        [1,2,3,4,5,6,7,8,9,10],
        ["home","about","career","home","cart","maps","home","home","about","career"]
    ) == ['home', 'about', 'career']