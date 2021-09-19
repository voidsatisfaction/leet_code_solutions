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
            else:
                if j == len(index_source_target_iterator)-1:
                    answer += s[i:]
                    i = len(s)
                else:
                    next_index = index_source_target_iterator[j+1][0]
                    answer += s[i:next_index]
                    i = next_index

        answer += s[i:]

        return answer

if __name__ == '__main__':
    s = Solution()

    assert s.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]) == "eeebffff"

    assert s.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]) == "eeecd"

    assert s.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]) == "vbfrssozp"
    
