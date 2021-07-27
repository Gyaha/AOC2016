def read_data(data: str) -> list:
    return [a.strip() for a in data.split(",")]


def find_distance(data: str) -> int:
    inst = read_data(data)
    y, x = 0, 0
    dir = 0
    for i in inst:
        dir = turn(dir, i[0])
        dist = int(i[1:])
        if dir == 0:
            y += dist
        elif dir == 1:
            x += dist
        elif dir == 2:
            y -= dist
        else:  # == 3:
            x -= dist
    return abs(y) + abs(x)


def turn(dir: int, i: str) -> int:
    if i == "R":
        dir += 1
    else:
        dir -= 1
    if dir < 0:
        dir = 3
    elif dir > 3:
        dir = 0
    return dir


def visited_twice(data: str) -> int:
    inst = read_data(data)
    y, x = 0, 0
    visited = set()
    dir = 0
    for i in inst:
        dir = turn(dir, i[0])
        dist = int(i[1:])
        y, x, done = travel(y, x, visited, dir, dist)
        if done:
            break
    return abs(y) + abs(x)


def travel(y, x, visited: set, dir, dist):
    for _ in range(dist):
        if dir == 0:
            y += 1
        elif dir == 1:
            x += 1
        elif dir == 2:
            y -= 1
        else:
            x -= 1
        if (y, x) in visited:
            return y, x, True
        else:
            visited.add((y, x))
    return y, x, False


with open("input01") as file:
    data = file.read()
    print(find_distance(data))
    print(visited_twice(data))
