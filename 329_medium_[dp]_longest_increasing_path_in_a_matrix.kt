import kotlin.math.max

class Solution {
    fun longestIncreasingPath(matrix: Array<IntArray>): Int {
        val m = matrix.size
        val n = matrix[0].size

        val dp = Array(m){ IntArray(n) { -1 } }
        val visited = Array(m){ BooleanArray(n) { false } }
        var maxLongestIncreasingPathLength = -1

        for (row in 0..m-1) {
            for (column in 0..n-1) {
                if (dp[row][column] == -1) {
                    dp[row][column] = getLongestIncreasingPathRec(row, column, matrix, dp, visited)
                }

                maxLongestIncreasingPathLength = max(maxLongestIncreasingPathLength, dp[row][column])
            }
        }

        return maxLongestIncreasingPathLength
    }

    fun getLongestIncreasingPathRec(row: Int, column: Int, matrix: Array<IntArray>, dp: Array<IntArray>, visited: Array<BooleanArray>): Int {
        if (dp[row][column] != -1) {
            return dp[row][column]
        }

        visited[row][column] = true

        val directionList = listOf(Pair(-1, 0), Pair(1, 0), Pair(0, -1), Pair(0, 1))

        var longestIncreasingPathLength = 1
        for (direction in directionList) {
            val nextRow = row + direction.first
            val nextColumn = column + direction.second
            
            if (
                nextRow == -1 ||
                nextColumn == -1 ||
                nextRow == matrix.size ||
                nextColumn == matrix[0].size ||
                visited[nextRow][nextColumn] ||
                matrix[row][column] >= matrix[nextRow][nextColumn]
            ) {
                continue
            }

            longestIncreasingPathLength = max(
                longestIncreasingPathLength,
                1 + getLongestIncreasingPathRec(nextRow, nextColumn, matrix, dp, visited)
            )
        }

        visited[row][column] = false

        dp[row][column] = longestIncreasingPathLength
        return dp[row][column]
    }
}