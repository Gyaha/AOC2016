import hashlib


def find_code(s: str) -> str:
    r, c = "", ""
    i = 0
    for _ in range(8):
        r, i = get_next_code(s, i)
        while not r[:5] == "00000":
            r, i = get_next_code(s, i)
        c += r[5]
    return c


def get_next_code(s, i):
    i += 1
    r = hashlib.md5((s + str(i)).encode()).hexdigest()
    return r, i


def get_next_valid_md5(s: str, i: int):
    r = ""
    while not r[:5] == "00000":
        i += 1
        r = hashlib.md5((s + str(i)).encode()).hexdigest()
    return r, i


def find_code_2(s: str) -> str:
    code = [0, 0, 0, 0, 0, 0, 0, 0]
    r, i = "", 0
    while not is_code_done(code):
        r, i = get_next_valid_md5(s, i)
        try_and_fit_into(code, r)
    return "".join(code)


def try_and_fit_into(c: list, r: str):
    l, p = r[6], r[5]
    if not p.isnumeric():
        return
    p = int(p)
    if not p <= 7:
        return
    if c[p] == 0:
        c[p] = l


def is_code_done(c: list):
    for a in c:
        if a == 0:
            return False
    return True


print(find_code("ffykfhsq"))
print(find_code_2("ffykfhsq"))
