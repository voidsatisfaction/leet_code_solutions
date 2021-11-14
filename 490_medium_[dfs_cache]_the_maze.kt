typealias CollisionCoordinates = Array<Array<MutableMap<Direction, Pair<Int, Int>>>>

enum class Direction {
    UP, DOWN, LEFT, RIGHT
}

class Solution {
    fun hasPath(maze: Array<IntArray>, start: IntArray, destination: IntArray): Boolean {
        val m = maze.size
        val n = maze[0].size

        val collisionCoordinates = getCollisionCoordinates(maze, m, n)

        val visited = Array(m) { Array(n) { false } }
        
        val row = start[0]
        val column = start[1]
        
        visited[row][column] = true

        return dfs(row, column, maze, visited, collisionCoordinates, destination)
    }

    private fun dfs(
        row: Int,
        column: Int,
        maze: Array<IntArray>,
        visited: Array<Array<Boolean>>,
        collisionCoordinates: CollisionCoordinates,
        destination: IntArray
    ): Boolean {
        if (row == destination[0] && column == destination[1]) {
            return true
        }
        
        var result = false
        for (direction in Direction.values()) {
            val nextRow = collisionCoordinates[row][column][direction]!!.first
            val nextColumn = collisionCoordinates[row][column][direction]!!.second
            
            if (!visited[nextRow][nextColumn]) {
                visited[nextRow][nextColumn] = true
                result = result || dfs(nextRow, nextColumn, maze, visited, collisionCoordinates, destination)
            }
        }

        return result
    }

    private fun getCollisionCoordinates(maze: Array<IntArray>, m: Int, n: Int): CollisionCoordinates {
        val collisionCoordinates = Array(m) { Array(n) { mutableMapOf<Direction, Pair<Int, Int>>() } }

        for (row in 0..m-1) {
            for (column in 0..n-1) {
                if (maze[row][column] == 1) {
                    continue
                }

                for (i in row downTo -1) {
                    if (i == -1 || maze[i][column] == 1) {
                        collisionCoordinates[row][column][Direction.UP] = Pair(i+1, column)
                        break
                    }
                }

                for (i in row until m+1) {
                    if (i == m || maze[i][column] == 1) {
                        collisionCoordinates[row][column][Direction.DOWN] = Pair(i-1, column)
                        break
                    }
                }

                for (i in column downTo -1) {
                    if (i == -1 || maze[row][i] == 1) {
                        collisionCoordinates[row][column][Direction.LEFT] = Pair(row, i+1)
                        break
                    }
                }

                for (i in column until n+1) {
                    if (i == n || maze[row][i] == 1) {
                        collisionCoordinates[row][column][Direction.RIGHT] = Pair(row, i-1)
                        break
                    }
                }
            }
        }

        return collisionCoordinates
    }
}