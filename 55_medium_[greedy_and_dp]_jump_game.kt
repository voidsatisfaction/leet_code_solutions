import kotlin.math.max

class Solution {
    fun canJump(nums: IntArray): Boolean {
        var maxIndex = 0
        var currentIndex = 0
        
        while (maxIndex >= currentIndex) {
            if (currentIndex == nums.size-1) {
                return true
            }

            maxIndex = max(maxIndex, currentIndex + nums[currentIndex])
            currentIndex += 1
        }

        return false
    }
}