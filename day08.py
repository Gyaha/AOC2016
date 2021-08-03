def read_data(d: str) -> list:
    return [a.split() for a in d.splitlines()]


def print_screen(s: list):
    for l in s:
        print("".join(["#" if a else "." for a in l]))


def create_screen(h: int, w: int):
    return [[0 for _ in range(w)]for _ in range(h)]


def screen_stuff(d: str, h: int, w: int) -> int:
    data = read_data(d)
    screen = create_screen(h, w)
    for l in data:
        if l[0] == "rect":
            w, h = l[1].split("x")
            w, h = int(w), int(h)
            rect(screen, h, w)
        elif l[0] == "rotate":
            dir = l[2][0]
            t = int(l[2][2:])
            n = int(l[4])
            rota(screen, dir, t, n)
    n = 0
    for l in screen:
        n += sum(l)
    return n, screen


def rect(s: list, h, w):
    for y in range(h):
        for x in range(w):
            if y < 0 or y >= len(s) or x < 0 or x >= len(s[0]):
                continue
            s[y][x] = 1


def rota(s: list, d: chr, t: int, n: int):
    for _ in range(n):
        if d == "y":
            rota_y(s, t)
        else:
            rota_x(s, t)


def rota_x(s: list, t: int):
    f = s[len(s) - 1][t]
    for i in range(len(s) - 1, 0, -1):
        s[i][t] = s[i - 1][t]
    s[0][t] = f


def rota_y(s: list, t: int):
    s[t] = [s[t][len(s[0]) - 1]] + s[t][:-1]


with open("input08") as file:
    d = file.read()
    lit, screen = screen_stuff(d, 6, 50)
    print(lit)
    print_screen(screen)
