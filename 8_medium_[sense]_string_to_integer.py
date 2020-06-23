class Solution:
    def myAtoi(self, str: str) -> int:
        INF = 2147483647
        MINUS_INF = -2147483648

        is_plus = True
        num_char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        trimmed_str = str.lstrip()

        if len(trimmed_str) == 0:
            return 0

        i = 0
        val = 0

        first_char = trimmed_str[0]
        if first_char == '-':
            is_plus = False
            i = 1
        elif first_char == '+':
            i = 1
        elif first_char in num_char_list:
            pass
        else:
            return 0

        for i in range(i, len(trimmed_str)):
            c = trimmed_str[i]

            if c in num_char_list:
                val = 10 * val + int(c)
            else:
                break

        if is_plus is True and val > INF:
            return INF

        if is_plus is False and val > -MINUS_INF:
            return MINUS_INF

        if is_plus is False:
            return -val
        
        return val



if __name__ == '__main__':
    assert Solution().myAtoi('42') == 42
    assert Solution().myAtoi('   -42') == -42
    assert Solution().myAtoi('4193 with words') == 4193
    assert Solution().myAtoi('words and 987') == 0
    assert Solution().myAtoi('-91283472332') == -2147483648
    assert Solution().myAtoi('01') == 1