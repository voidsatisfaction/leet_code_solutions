from typing import Tuple, List

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def extract_file_name_with_depth(raw_file_name: str) -> Tuple[str, int]:
            i = 0
            depth = 1

            while True:
                if raw_file_name[i] == "\t":
                    depth += 1
                    i += 1
                else:
                    return (raw_file_name[i:], depth)

        def get_current_depth(file_path_stack: List[str]) -> int:
            return len(file_path_stack)

        def is_file(file_name: str) -> bool:
            return len(file_name.split('.')) >= 2

        def get_absolute_path(file_path_stack: List[str]) -> str:
            return "/".join(file_path_stack)

        raw_file_name_list = input.split("\n")

        file_name_with_depth_list = []
        for raw_file_name in raw_file_name_list:
            file_name_with_depth_list.append(
                extract_file_name_with_depth(raw_file_name)
            )

        answer = 0
        file_path_stack = []
        for file_name, depth in file_name_with_depth_list:
            while get_current_depth(file_path_stack) >= depth:
                file_path_stack.pop()

            file_path_stack.append(file_name)
            if is_file(file_name):
                answer = max(answer, len(get_absolute_path(file_path_stack)))

        return answer


if __name__ == '__main__':
    s = Solution()

    assert s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32

    assert s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20

    assert s.lengthLongestPath("a") == 0

    assert s.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt") == 12
