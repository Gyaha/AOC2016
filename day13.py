def get_wall(x: int, y: int, f: int) -> bool:
    n = (x * x) + (3 * x) + (2 * x * y) + (y) + (y * y) + f
    return not (bin(n)[2:].count("1") % 2 == 0)


class pf_node():
    def __init__(self) -> None:
        self.pos = (0, 0)
        self.is_wall = False
        self.enter_from = (0, 0)
        self.distance_traveled = 0

    def __repr__(self) -> str:
        return str(self.is_wall)


def get_neighbors(pos) -> list:
    x = pos[0]
    y = pos[1]
    n = []
    if x > 0:
        n.append((x - 1, y))
    if y > 0:
        n.append((x, y - 1))
    n.append((x + 1, y))
    n.append((x, y + 1))
    return n


def get_node(pos, f, map) -> pf_node:
    node = None
    if pos in map.keys():
        node = map[pos]
    else:
        node = pf_node()
        node.is_wall = get_wall(pos[0], pos[1], f)
        node.pos = pos
        map[pos] = node
    return node


def pf_this(sx, sy, ex, ey, f):
    _map = {}
    visited = []
    start = (sx, sy)
    target = (ex, ey)
    queue = [start]
    while len(queue):
        current = queue.pop(0)
        visited.append(current)
        current_node = get_node(current, f, _map)
        if current == target:
            return current_node.distance_traveled
        if current_node.is_wall:
            continue
        current_dist = current_node.distance_traveled + 1
        neighbors = get_neighbors(current)
        for n in neighbors:
            if n in visited:
                continue
            queue.append(n)
            nn = get_node(n, f, _map)
            if not nn.distance_traveled < current_dist:
                continue
            nn.enter_from = current
            nn.distance_traveled = current_dist


def pf_count(sx, sy, r, f):
    _map = {}
    visited = []
    start = (sx, sy)
    queue = [start]
    while len(queue):
        current = queue.pop(0)
        visited.append(current)
        current_node = get_node(current, f, _map)
        if current_node.distance_traveled >= r:
            continue
        if current_node.is_wall:
            continue
        current_dist = current_node.distance_traveled + 1
        neighbors = get_neighbors(current)
        for n in neighbors:
            if n in visited:
                continue
            queue.append(n)
            nn = get_node(n, f, _map)
            if not nn.distance_traveled < current_dist:
                continue
            nn.enter_from = current
            nn.distance_traveled = current_dist
    n = 0
    for a in _map.values():
        if not a.is_wall:
            n += 1
    return n


print(pf_this(1, 1, 31, 39, 1362))
print(pf_count(1, 1, 50, 1362))
