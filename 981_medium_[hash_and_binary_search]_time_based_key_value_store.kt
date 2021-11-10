class TimeMap() {
    private val keyValueStore = mutableMapOf<String, ArrayList<Pair<String, Int>>>()

    fun set(key: String, value: String, timestamp: Int) {
        when (keyValueStore[key]) {
            null -> keyValueStore[key] = arrayListOf(Pair(value, timestamp))
            else -> keyValueStore[key]!!.add(Pair(value, timestamp))
        }
    }

    fun get(key: String, timestamp: Int): String {
        val array = keyValueStore[key]
        if (array == null) {
            return ""
        }

        val index = findSameOrSmallTimestampElementIndex(key, timestamp)

        val result = when (index) {
            -1 -> ""
            else -> array[index].first
        }

        return result
    }

    private fun findSameOrSmallTimestampElementIndex(key: String, timestamp: Int): Int {
        val array = keyValueStore[key]!!

        if (array.isEmpty()) {
            return -1
        }

        var low = 0
        var high = array.size

        while (low < high) {
            val mid = (low + high) / 2

            val targetTimestamp = array[mid].second
            if (timestamp == targetTimestamp) {
                return mid
            } else if (timestamp < targetTimestamp) {
                high = mid
            } else {
                low = mid + 1
            }
        }

        if (low == 0 && array[0].second > timestamp) {
            return -1
        }

        return low-1
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */