import java.util.ArrayDeque

class Solution {
    data class Element(val value: Int, val index: Int)

    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        var answer = IntArray(nums.size-k+1)
        var deque = ArrayDeque<Element>()

        var i = 0
        var j = k-1

        for (l in 0..j) {
            val element = Element(nums[l], l)

            addNewNumber(deque, element)
        }

        while (j <= nums.size-1) {
            answer[i] = deque.first().value
            
            if (j == nums.size-1) {
                break
            }
            
            addNewNumber(deque, Element(nums[j+1], j+1))
            removeNumberUntil(deque, i)

            i += 1
            j += 1
        }

        return answer
    }

    private fun addNewNumber(deque: ArrayDeque<Element>, element: Element): Unit {
        if (deque.isEmpty()) {
            deque.add(element)
        } else {
            while (!deque.isEmpty() && deque.last().value <= element.value) {
                deque.removeLast()
            }
            deque.addLast(element)
        }
    }

    private fun removeNumberUntil(deque: ArrayDeque<Element>, index: Int): Unit {
        while (!deque.isEmpty() && index >= deque.first().index) {
            deque.removeFirst()
        }
    }
}