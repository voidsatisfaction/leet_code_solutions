class Solution {
    fun setZeroes(matrix: Array<IntArray>): Unit {
        val n = matrix.size
        val m = matrix[0].size

        val numberSet = mutableSetOf<Int>()
        for (row in 0..n-1) {
            for (col in 0..m-1) {
                numberSet.add(matrix[row][col])
            }
        }
        
        var idleNumber = 0
        for (i in 0..(n*m)) {
            if (!numberSet.contains(i)) {
                idleNumber = i
                break
            }
        }

        for (row in 0..n-1) {
            for (col in 0..m-1) {
                if (matrix[row][col] == 0) {
                    setRowToMinusOneExceptZero(matrix, row, idleNumber)
                    continue
                }
            }
        }

        for (row in 0..n-1) {
            for (col in 0..m-1) {
                if (matrix[row][col] == 0) {
                    setColToMinusOneExceptZero(matrix, col, idleNumber)
                    continue
                }
            }
        }

        for (row in 0..n-1) {
            for (col in 0..m-1) {
                if (matrix[row][col] == idleNumber) {
                    matrix[row][col] = 0
                }
            }
        }
    }

    private fun setRowToMinusOneExceptZero(matrix: Array<IntArray>, row: Int, idleNumber: Int): Unit {
        val m = matrix[0].size

        for (col in 0..m-1) {
            if (matrix[row][col] != 0) {
                matrix[row][col] = idleNumber
            }
        }
    }

    private fun setColToMinusOneExceptZero(matrix: Array<IntArray>, col: Int, idleNumber: Int): Unit {
        val n = matrix.size

        for (row in 0..n-1) {
            if (matrix[row][col] != 0) {
                matrix[row][col] = idleNumber
            }
        }
    }
}