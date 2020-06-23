class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INF = 2**31-1
        MINUS_INF = -2**31
        is_plus = (dividend>0 and divisor>0) or (dividend<0 and divisor<0)

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        if dividend == MINUS_INF and divisor == -1:
            return INF

        if abs_divisor > abs_dividend:
            return 0

        nums = [0, abs_divisor]
        while nums[-1] + nums[-1] <= abs_dividend:
            nums.append(nums[-1]+nums[-1])

        answer = 0
        while True:
            left, right = 0, len(nums)-1

            while left <= right:
                mid = (left + right) // 2

                if mid == len(nums)-1 or (nums[mid+1] > abs_dividend and nums[mid] <= abs_dividend):
                    if mid == 0:
                        if is_plus:
                            return answer
                        else:
                            return -answer

                    answer += 2**(mid-1)
                    abs_dividend -= nums[mid]
                    nums = nums[:mid]
                    break

                if nums[mid] > abs_dividend:
                    right = mid-1
                else:
                    left = mid+1

            

if __name__ == '__main__':
    assert Solution().divide(10, 3) == 3
    assert Solution().divide(7, -3) == -2
    assert Solution().divide(-2**31, -1) == 2**31-1