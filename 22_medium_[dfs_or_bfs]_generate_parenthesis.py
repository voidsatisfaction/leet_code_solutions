from typing import List
from queue import Queue

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        states = Queue()
        states.put({ 'parentheses': '(', 'open_nums': 1, 'closed_nums': 0 })

        break_flag = False
        while break_flag is False:
            length = states.qsize()

            for _ in range(length):
                state = states.get()
                open_nums = state['open_nums']
                closed_nums = state['closed_nums']

                if open_nums == n and closed_nums == n:
                    states.put(state)
                    break_flag = True
                    break

                if open_nums == n:
                    state['parentheses'] += ')'
                    state['closed_nums'] += 1
                    states.put(state)
                elif open_nums == closed_nums:
                    state['parentheses'] += '('
                    state['open_nums'] += 1
                    states.put(state)
                else:
                    next_parentheses1 = state['parentheses'] + '('
                    next_open_nums1 = open_nums + 1
                    next_closed_nums1 = closed_nums

                    states.put({
                        'parentheses': next_parentheses1,
                        'open_nums': next_open_nums1,
                        'closed_nums': next_closed_nums1
                    })

                    next_parentheses2 = state['parentheses'] + ')'
                    next_open_nums2 = open_nums
                    next_closed_nums2 = closed_nums + 1

                    states.put({
                        'parentheses': next_parentheses2,
                        'open_nums': next_open_nums2,
                        'closed_nums': next_closed_nums2
                    })

        answer = []
        while not states.empty():
            state = states.get()

            answer.append(state['parentheses'])

        return answer

if __name__ == '__main__':
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(3))

    print(Solution().generateParenthesis(10))