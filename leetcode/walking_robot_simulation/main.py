"""
A robot on an infinite XY-plane starts at point (0, 0) and faces north. The robot can receive one of three possible types of commands:

    -2: turn left 90 degrees,
    -1: turn right 90 degrees, or
    1 <= k <= 9: move forward k units.

Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi).

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the maximum Euclidean distance that the robot will be from the origin squared (i.e. if the distance is 5, return 25).
"""
from typing import List


def robot_sim(commands: List[int], obstacles: List[List[int]]) -> int:
    positions_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    obstacles = set(map(tuple, obstacles))
    x, y, direction, max_d = 0, 0, 0, 0

    for command in commands:
        if command == -2:
            direction = (direction - 1) % 4
        elif command == -1:
            direction = (direction + 1) % 4
        else:
            x_offset, y_offset = positions_offset[direction]
            while command:
                if (x + x_offset, y + y_offset) not in obstacles:
                    x += x_offset
                    y += y_offset
                command -= 1
            max_d = max(max_d, x ** 2 + y ** 2)
    return max_d


if __name__ == '__main__':
    print(robot_sim([4, -1, 4, -2, 4], [[2, 4]]))
    print(robot_sim([4, -1, 3], []))
