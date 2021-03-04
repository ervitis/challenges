"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.
"""


def is_path_crossing(path: str) -> bool:
    mat = [[0, 0]]

    x, y = 0, 0
    for p in path:
        if p == 'N':
            y += 1
        elif p == 'E':
            x += 1
        elif p == 'W':
            x -= 1
        else:
            y -= 1

        if [x, y] in mat:
            return True
        else:
            mat.append([x, y])
    return False


if __name__ == '__main__':
    print(is_path_crossing('NES'))
    print(is_path_crossing('NESWW'))
