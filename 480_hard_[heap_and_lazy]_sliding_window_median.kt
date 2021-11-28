import kotlin.math.*
import java.util.*

data class IntegerNumber(
    val index: Int,
    val value: Int,
    var removed: Boolean = false
)

class MedianFinder {
    private var maxHeap = PriorityQueue<IntegerNumber> { integerNumber1, integerNumber2 ->
        if (integerNumber1.value > 0 && integerNumber2.value < 0) {
            -1
        } else if (integerNumber1.value < 0 && integerNumber2.value > 0) {
            1
        } else {
            integerNumber2.value - integerNumber1.value
        }
    }
    private var actualMaxHeapSize = 0

    private var minHeap = PriorityQueue<IntegerNumber> { integerNumber1, integerNumber2 ->
        if (integerNumber1.value > 0 && integerNumber2.value < 0) {
            1
        } else if (integerNumber1.value < 0 && integerNumber2.value > 0) {
            -1
        } else {
            integerNumber1.value - integerNumber2.value
        }
    }
    private var actualMinHeapSize = 0

    private var index_to_integer_number_map = mutableMapOf<Int, IntegerNumber>()

    fun addNum(index: Int, num: Int) {
        val integerNumberObject = IntegerNumber(index, num)
        if (minHeap.isEmpty() || num > minHeap.peek().value) {
            minHeap.add(integerNumberObject)
            actualMinHeapSize += 1
        } else {
            maxHeap.add(integerNumberObject)
            actualMaxHeapSize += 1
        }
        index_to_integer_number_map[index] = integerNumberObject
    }

    fun removeNumIndex(index: Int) {
        var integerNumberObject = index_to_integer_number_map[index]!!
        integerNumberObject.removed = true
        
        if (minHeap.isNotEmpty() && integerNumberObject.value >= minHeap.peek().value) {
            actualMinHeapSize -= 1
        } else {
            actualMaxHeapSize -= 1
        }
    }

    fun findMedian(): Double {
        truncateTopRemovedIntegerNumber()

        if (actualMinHeapSize == actualMaxHeapSize) {
            return (minHeap.peek().value.toDouble() + maxHeap.peek().value) / 2
        }

        if (actualMinHeapSize > actualMaxHeapSize) {
            return minHeap.peek().value.toDouble()
        }

        return maxHeap.peek().value.toDouble()
    }

    fun reconcile() {
        if (!shouldReconcile()) return

        if (actualMinHeapSize > actualMaxHeapSize) {
            val integerNumber = minHeap.poll()
            maxHeap.add(integerNumber)
            actualMinHeapSize -= 1
            actualMaxHeapSize += 1
        } else {
            val integerNumber = maxHeap.poll()
            minHeap.add(integerNumber)
            actualMaxHeapSize -= 1
            actualMinHeapSize += 1
        }
    }

    fun truncateTopRemovedIntegerNumber() {
        while (minHeap.isNotEmpty() && minHeap.peek().removed == true) {
            minHeap.poll()
        }

        while (maxHeap.isNotEmpty() && maxHeap.peek().removed == true) {
            maxHeap.poll()
        }
    }

    private fun shouldReconcile(): Boolean {
        return abs(actualMaxHeapSize - actualMinHeapSize) >= 2
    }
}


class Solution {
    fun medianSlidingWindow(nums: IntArray, k: Int): DoubleArray {
        val medianFinder = MedianFinder()
        var answer = DoubleArray(nums.size - k + 1)

        var i = 0
        var j = k-1

        for (l in 0..j) {
            medianFinder.addNum(l, nums[l])
            medianFinder.reconcile()
        }

        while (j < nums.size) {
            val median = medianFinder.findMedian()
            answer[i] = median

            if (j+1 == nums.size) {
                break
            }

            medianFinder.removeNumIndex(i)
            medianFinder.reconcile()
            medianFinder.addNum(j+1, nums[j+1])

            medianFinder.truncateTopRemovedIntegerNumber()
            medianFinder.reconcile()
            medianFinder.truncateTopRemovedIntegerNumber()

            i += 1
            j += 1
        }

        return answer
    }
}