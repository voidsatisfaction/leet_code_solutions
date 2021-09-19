from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        index_source_target_iterator = sorted(zip(indices, sources, targets))

        should_replace_target_list = []

        for index, source, _ in index_source_target_iterator:
            should_replace_target_list.append(
                s[index:index+len(source)] == source
            )
        
        answer, i = '', 0
        for j, (index, source, target) in enumerate(index_source_target_iterator):
            answer += s[i:index]
            i = index

            if should_replace_target_list[j] is True:
                answer += target
                i += len(source)

        answer += s[i:]

        return answer

if __name__ == '__main__':
    s = Solution()

    assert s.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]) == "eeebffff"

    assert s.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]) == "eeecd"

    assert s.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]) == "vbfrssozp"
    
