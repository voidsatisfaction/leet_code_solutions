from typing import List, Tuple

UP, DOWN, LEFT, RIGHT = "U", "D", "L", "R"

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        location, direction = [0, 0], UP
        while True:
            for instruction in instructions:
                location, direction = self._move(instruction, location, direction)

            if direction == UP and location == [0, 0]:
                return True
            elif direction == UP:
                return False
        
    def _move(self, instruction: str, location: List[int], direction: str) -> Tuple[List[int], str]:
        if direction == UP:
            if instruction == "G":
                location[1] += 1
            elif instruction == "L":
                direction = LEFT
            else:
                direction = RIGHT
        elif direction == DOWN:
            if instruction == "G":
                location[1] -= 1
            elif instruction == "L":
                direction = RIGHT
            else:
                direction = LEFT
        elif direction == LEFT:
            if instruction == "G":
                location[0] -= 1
            elif instruction == "L":
                direction = DOWN
            else:
                direction = UP
        else:
            if instruction == "G":
                location[0] += 1
            elif instruction == "L":
                direction = UP
            else:
                direction = DOWN

        return location, direction

if __name__ == '__main__':
    s = Solution()

    assert s.isRobotBounded("G") is False

    assert s.isRobotBounded("GGLLGG") is True

    assert s.isRobotBounded("GG") is False

    assert s.isRobotBounded("GL") is True
