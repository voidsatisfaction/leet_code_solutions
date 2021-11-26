import kotlin.math.*
import java.util.*

class MedianFinder() {
    val maxHeap = PriorityQueue<Int>(Collections.reverseOrder())
    val minHeap = PriorityQueue<Int>()

    fun addNum(num: Int) {
        if (minHeap.isEmpty() || num > minHeap.peek()) {
            minHeap.add(num)
        } else {
            maxHeap.add(num)
        }

        reconcile()
    }

    fun findMedian(): Double {
        if (minHeap.size == maxHeap.size) {
            return (minHeap.peek().toDouble() + maxHeap.peek()) / 2
        }

        if (minHeap.size > maxHeap.size) {
            return minHeap.peek().toDouble()
        }

        return maxHeap.peek().toDouble()
    }

    private fun reconcile() {
        if (!shouldReconcile()) return

        if (minHeap.size > maxHeap.size) {
            val num = minHeap.poll()
            maxHeap.add(num)
        } else {
            val num = maxHeap.poll()
            minHeap.add(num)
        }
    }

    private fun shouldReconcile(): Boolean {
        return abs(maxHeap.size - minHeap.size) >= 2
    }
}
